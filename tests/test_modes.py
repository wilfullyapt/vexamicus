"""Tests for dog modes enum."""

from vexamicus.modes import HOLD_MODES, LOCOMOTION_MODES, DogMode


def test_all_modes_unique_values():
    values = [m.value for m in DogMode]
    assert len(values) == len(set(values))


def test_hold_and_loco_partition():
    assert DogMode.STOP in HOLD_MODES
    assert DogMode.HEEL in LOCOMOTION_MODES
    assert HOLD_MODES.isdisjoint(LOCOMOTION_MODES)
