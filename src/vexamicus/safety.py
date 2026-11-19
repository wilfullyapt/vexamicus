"""Arming and e-stop policy."""

from __future__ import annotations


class SafetyError(RuntimeError):
    """Raised when a motion command violates safety policy."""


class SafetyGate:
    """Tracks armed + e-stop. Default is disarmed."""

    def __init__(self, *, armed: bool = False) -> None:
        self._armed = bool(armed)
        self._estopped = False

    @property
    def armed(self) -> bool:
        return self._armed and not self._estopped

    @property
    def estopped(self) -> bool:
        return self._estopped

    def arm(self) -> None:
        if self._estopped:
            raise SafetyError("clear e-stop before arming")
        self._armed = True

    def disarm(self) -> None:
        self._armed = False

    def estop(self) -> None:
        self._estopped = True
        self._armed = False

    def clear_estop(self) -> None:
        self._estopped = False

    def require_armed(self, *, context: str = "motion") -> None:
        if self._estopped:
            raise SafetyError(f"{context} blocked: e-stop active")
        if not self._armed:
            raise SafetyError(f"{context} blocked: disarmed (set armed: true to enable)")
