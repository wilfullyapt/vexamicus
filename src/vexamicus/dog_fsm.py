"""Dog behavior FSM (high-level modes on the body)."""

from __future__ import annotations

from dataclasses import dataclass

from vexamicus.hop import HopController
from vexamicus.modes import HOLD_MODES, LOCOMOTION_MODES, DogMode
from vexamicus.types import MotionState


@dataclass(frozen=True)
class TransitionResult:
    ok: bool
    mode: DogMode
    reason: str = ""


class DogBehavior:
    """Maps dog modes to motion intents."""

    def __init__(self, hop: HopController, *, mode: DogMode = DogMode.STOP) -> None:
        self.hop = hop
        self.mode = mode
        self._follow_gain = 0.0  # 0..1 placeholder for L2 policy hook

    def emergency_stop(self) -> TransitionResult:
        """Hard e-stop — bus stays latched until a new bus is constructed."""
        self.hop.bus.estop()
        self.mode = DogMode.STOP
        self._follow_gain = 0.0
        return TransitionResult(ok=True, mode=self.mode, reason="estop")

    def set_mode(self, mode: DogMode | str) -> TransitionResult:
        target = mode if isinstance(mode, DogMode) else DogMode(str(mode).strip().lower())
        if target is self.mode:
            return TransitionResult(ok=True, mode=self.mode, reason="already")

        if self.hop.bus.read_state().estopped and target is not DogMode.STOP:
            return TransitionResult(ok=False, mode=self.mode, reason="estopped")

        self.mode = target
        if target is DogMode.JUMP:
            self.hop.queue_jump()
            self._follow_gain = 0.0
        elif target in HOLD_MODES:
            # Soft stop / sit / stay: zero cmds without latching e-stop
            self._follow_gain = 0.0
            self.hop.bus.set_leg_extension(0.0)
            self.hop.bus.set_reaction_wheel_torque(0.0)
        elif target in LOCOMOTION_MODES:
            self._follow_gain = 0.5 if target is DogMode.HEEL else 0.8
            # Phase 0: locomotion is policy gain only — no planar drive yet
            self.hop.bus.set_reaction_wheel_torque(0.05 * self._follow_gain)
        else:
            self._follow_gain = 0.0
        return TransitionResult(ok=True, mode=self.mode, reason="ok")

    def tick(self, dt_s: float = 0.01) -> MotionState:
        return self.hop.tick(dt_s)

    def status(self) -> dict:
        state = self.hop.bus.read_state()
        return {
            "mode": self.mode.value,
            "follow_gain": self._follow_gain,
            "motion": state.as_dict(),
        }
