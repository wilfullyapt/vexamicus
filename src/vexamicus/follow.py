"""Follow policy stub (L2) — synthetic target envelope."""

from __future__ import annotations

from dataclasses import dataclass

from vexamicus.modes import DogMode


@dataclass
class FollowTarget:
    """Owner (or beacon) pose in body frame — phase 0 synthetic."""

    x_m: float = 0.0
    y_m: float = 0.0
    valid: bool = True


@dataclass
class FollowCommand:
    """Output of follow policy for a motion layer that does not yet exist."""

    forward_m_s: float = 0.0
    yaw_rate_rad_s: float = 0.0
    lose_target: bool = False


class FollowPolicy:
    """Keep a leash radius; pure math, no sensors."""

    def __init__(self, *, leash_m: float = 1.5, max_speed_m_s: float = 0.8) -> None:
        self.leash_m = leash_m
        self.max_speed_m_s = max_speed_m_s

    def step(self, mode: DogMode, target: FollowTarget) -> FollowCommand:
        if not target.valid:
            return FollowCommand(lose_target=True)
        if mode in {DogMode.STOP, DogMode.SIT, DogMode.STAY, DogMode.JUMP}:
            return FollowCommand()
        dist = (target.x_m**2 + target.y_m**2) ** 0.5
        if dist <= self.leash_m and mode is DogMode.HEEL:
            return FollowCommand()
        # Proportional chase toward target in body frame (+x forward)
        scale = min(1.0, max(0.0, (dist - self.leash_m * 0.5) / max(self.leash_m, 1e-6)))
        speed = self.max_speed_m_s * scale
        if dist < 1e-6:
            return FollowCommand()
        forward = speed * (target.x_m / dist)
        # yaw toward target (small-angle stand-in)
        yaw = 1.5 * (target.y_m / dist)
        if mode is DogMode.ORBIT:
            # circle: prefer tangential
            return FollowCommand(forward_m_s=0.3 * speed, yaw_rate_rad_s=0.9)
        return FollowCommand(forward_m_s=forward, yaw_rate_rad_s=yaw)
