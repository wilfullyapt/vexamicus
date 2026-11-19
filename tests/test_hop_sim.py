"""Hop controller tests."""

from vexamicus.hop import HopController
from vexamicus.motion_bus import SimMotionBus


def test_run_jumps_completes():
    bus = SimMotionBus()
    hop = HopController(bus)
    metrics = hop.run_jumps(2, dt_s=0.01, max_steps=8000)
    assert metrics.hops >= 2
    assert metrics.peak_height_m > 0.0
