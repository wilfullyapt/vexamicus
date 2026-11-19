"""MotionBus + safety tests."""

import pytest

from vexamicus.motion_bus import HwMotionBus, SimMotionBus, make_motion_bus
from vexamicus.safety import SafetyError, SafetyGate
from vexamicus.types import HopPhase


def test_sim_tick_idle():
    bus = SimMotionBus()
    st = bus.tick(0.01)
    assert st.height_m == 0.0
    assert st.phase in {HopPhase.IDLE, HopPhase.STANCE}


def test_sim_jump_leaves_ground():
    bus = SimMotionBus()
    bus.set_leg_extension(0.9)
    bus.request_jump()
    airborne = False
    peak = 0.0
    for _ in range(200):
        st = bus.tick(0.01)
        peak = max(peak, st.height_m)
        if st.height_m > 0.01:
            airborne = True
    assert airborne
    assert peak > 0.05
    assert bus.read_state().hop_count >= 1


def test_estop_zeros():
    bus = SimMotionBus()
    bus.set_leg_extension(1.0)
    bus.estop()
    st = bus.read_state()
    assert st.estopped
    assert st.leg_extension == 0.0
    bus.request_jump()
    bus.tick(0.01)
    assert bus.read_state().hop_count == 0


def test_hw_requires_allow():
    with pytest.raises(SafetyError):
        HwMotionBus()


def test_hw_refuses_even_when_armed():
    gate = SafetyGate(armed=True)
    bus = HwMotionBus(safety=gate, allow_hw=True)
    with pytest.raises(SafetyError):
        bus.set_leg_extension(0.5)


def test_make_motion_bus_sim():
    bus = make_motion_bus("sim")
    assert isinstance(bus, SimMotionBus)


def test_safety_require_armed():
    g = SafetyGate(armed=False)
    with pytest.raises(SafetyError):
        g.require_armed()
    g.arm()
    g.require_armed()
