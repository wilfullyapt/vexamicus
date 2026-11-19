"""MotionBus HAL — sim default; hw refuse-stub."""

from __future__ import annotations

from abc import ABC, abstractmethod

from vexamicus.safety import SafetyError, SafetyGate
from vexamicus.types import HopPhase, MotionState


class MotionBus(ABC):
    """Actuator surface for leg + reaction wheel."""

    @abstractmethod
    def set_leg_extension(self, ratio: float) -> None:
        """Set leg extension command in [0, 1]."""

    @abstractmethod
    def set_reaction_wheel_torque(self, torque: float) -> None:
        """Set reaction-wheel torque command (N·m or sim units)."""

    @abstractmethod
    def estop(self) -> None:
        """Zero actuators immediately."""

    @abstractmethod
    def read_state(self) -> MotionState:
        """Return latest state snapshot."""

    @abstractmethod
    def tick(self, dt_s: float) -> MotionState:
        """Advance plant by dt (sim) or sample sensors (hw)."""


def _clamp01(x: float) -> float:
    return 0.0 if x < 0.0 else 1.0 if x > 1.0 else float(x)


class SimMotionBus(MotionBus):
    """Integrates a tiny vertical hopper plant for desk/CI."""

    def __init__(
        self,
        *,
        gravity_m_s2: float = 9.81,
        mass_kg: float = 0.12,
        spring_k: float = 180.0,
        max_extension_m: float = 0.12,
        safety: SafetyGate | None = None,
    ) -> None:
        self.gravity_m_s2 = gravity_m_s2
        self.mass_kg = mass_kg
        self.spring_k = spring_k
        self.max_extension_m = max_extension_m
        self.safety = safety or SafetyGate(armed=False)
        # Sim allows kinematic tick without arm; torque/extension cmds still recorded.
        self._leg_cmd = 0.0
        self._rw_cmd = 0.0
        self._height = 0.0
        self._vz = 0.0
        self._phase = HopPhase.IDLE
        self._hop_count = 0
        self._peak = 0.0
        self._flight_time = 0.0
        self._last_flight = 0.0
        self._pending_jump = False
        self._estopped = False

    def request_jump(self) -> None:
        """Queue a hop impulse on next stance opportunity."""
        if self._estopped:
            return
        self._pending_jump = True

    def set_leg_extension(self, ratio: float) -> None:
        if self._estopped:
            return
        self._leg_cmd = _clamp01(ratio)

    def set_reaction_wheel_torque(self, torque: float) -> None:
        if self._estopped:
            return
        self._rw_cmd = float(torque)

    def estop(self) -> None:
        self._estopped = True
        self._leg_cmd = 0.0
        self._rw_cmd = 0.0
        self._pending_jump = False
        self._vz = 0.0
        self.safety.estop()

    def read_state(self) -> MotionState:
        return MotionState(
            leg_extension=self._leg_cmd,
            reaction_wheel_torque=self._rw_cmd,
            height_m=self._height,
            vertical_vel_m_s=self._vz,
            phase=self._phase,
            hop_count=self._hop_count,
            peak_height_m=self._peak,
            last_flight_time_s=self._last_flight,
            estopped=self._estopped,
        )

    def tick(self, dt_s: float) -> MotionState:
        if dt_s <= 0:
            return self.read_state()
        if self._estopped:
            self._phase = HopPhase.IDLE
            return self.read_state()

        # Launch from ground when jump pending.
        if self._pending_jump and self._height <= 1e-6:
            # Spring energy ~ 0.5 k x^2 → v = sqrt(k/m) * x * scale from leg_cmd
            x = max(self._leg_cmd, 0.35) * self.max_extension_m
            energy = 0.5 * self.spring_k * x * x
            self._vz = (2.0 * energy / self.mass_kg) ** 0.5
            self._height = 1e-4
            self._phase = HopPhase.FLIGHT
            self._hop_count += 1
            self._flight_time = 0.0
            self._pending_jump = False
            self._peak = self._height

        if self._phase == HopPhase.FLIGHT or self._height > 0:
            self._phase = HopPhase.FLIGHT
            self._vz -= self.gravity_m_s2 * dt_s
            self._height += self._vz * dt_s
            self._flight_time += dt_s
            if self._height > self._peak:
                self._peak = self._height
            if self._height <= 0.0:
                self._height = 0.0
                self._vz = 0.0
                self._last_flight = self._flight_time
                self._phase = HopPhase.STANCE
                self._flight_time = 0.0
        else:
            self._phase = HopPhase.IDLE if not self._pending_jump else HopPhase.STANCE

        return self.read_state()


class HwMotionBus(MotionBus):
    """Placeholder hardware backend — refuses live torque in phase 0."""

    def __init__(self, *, safety: SafetyGate | None = None, allow_hw: bool = False) -> None:
        if not allow_hw:
            raise SafetyError(
                "HwMotionBus blocked: pass allow_hw=True only on a reviewed device path"
            )
        self.safety = safety or SafetyGate(armed=False)
        self._state = MotionState()

    def set_leg_extension(self, ratio: float) -> None:
        self.safety.require_armed(context="hw leg")
        raise SafetyError("hw leg driver not implemented (phase 0)")

    def set_reaction_wheel_torque(self, torque: float) -> None:
        self.safety.require_armed(context="hw reaction wheel")
        raise SafetyError("hw reaction-wheel driver not implemented (phase 0)")

    def estop(self) -> None:
        self.safety.estop()
        self._state = MotionState(estopped=True)

    def read_state(self) -> MotionState:
        return self._state

    def tick(self, dt_s: float) -> MotionState:
        _ = dt_s
        return self.read_state()


def make_motion_bus(
    backend: str = "sim",
    *,
    armed: bool = False,
    allow_hw: bool = False,
    **sim_kwargs: float,
) -> MotionBus:
    safety = SafetyGate(armed=armed)
    name = (backend or "sim").strip().lower()
    if name == "sim":
        return SimMotionBus(safety=safety, **sim_kwargs)  # type: ignore[arg-type]
    if name == "hw":
        return HwMotionBus(safety=safety, allow_hw=allow_hw)
    raise ValueError(f"unknown motion backend: {backend!r}")
