"""Dog / body high-level modes."""

from __future__ import annotations

from enum import Enum


class DogMode(str, Enum):
    """Commandable body modes (L3 lane)."""

    STOP = "stop"
    SIT = "sit"
    STAY = "stay"
    COME = "come"
    HEEL = "heel"
    JUMP = "jump"
    ORBIT = "orbit"
    FREE = "free"


# Modes that request locomotion toward / around a target (follow-ish).
LOCOMOTION_MODES = frozenset({DogMode.COME, DogMode.HEEL, DogMode.ORBIT, DogMode.FREE})

# Modes that should hold position / not hop unless commanded.
HOLD_MODES = frozenset({DogMode.STOP, DogMode.SIT, DogMode.STAY})
