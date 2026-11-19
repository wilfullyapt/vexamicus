"""Shared motion / telemetry types."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class HopPhase(str, Enum):
    STANCE = "stance"
    FLIGHT = "flight"
    IDLE = "idle"


@dataclass(frozen=True)
class MotionState:
    """Snapshot of actuator + hop plant (sim or hw)."""

    leg_extension: float = 0.0  # 0..1
    reaction_wheel_torque: float = 0.0
    height_m: float = 0.0
    vertical_vel_m_s: float = 0.0
    phase: HopPhase = HopPhase.IDLE
    hop_count: int = 0
    peak_height_m: float = 0.0
    last_flight_time_s: float = 0.0
    estopped: bool = False

    def as_dict(self) -> dict:
        return {
            "leg_extension": self.leg_extension,
            "reaction_wheel_torque": self.reaction_wheel_torque,
            "height_m": self.height_m,
            "vertical_vel_m_s": self.vertical_vel_m_s,
            "phase": self.phase.value,
            "hop_count": self.hop_count,
            "peak_height_m": self.peak_height_m,
            "last_flight_time_s": self.last_flight_time_s,
            "estopped": self.estopped,
        }


@dataclass
class HopMetrics:
    """Aggregate metrics over a sim run."""

    hops: int = 0
    peak_height_m: float = 0.0
    total_flight_time_s: float = 0.0
    samples: list[MotionState] = field(default_factory=list)
