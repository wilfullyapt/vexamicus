"""Dog FSM tests."""

from vexamicus.dog_fsm import DogBehavior
from vexamicus.hop import HopController
from vexamicus.modes import DogMode
from vexamicus.motion_bus import SimMotionBus


def test_set_heel_and_stop():
    dog = DogBehavior(HopController(SimMotionBus()))
    r = dog.set_mode(DogMode.HEEL)
    assert r.ok and dog.mode is DogMode.HEEL
    r2 = dog.set_mode(DogMode.STOP)
    assert r2.ok and dog.mode is DogMode.STOP
    # soft stop must not latch e-stop
    assert not dog.hop.bus.read_state().estopped
    assert dog.set_mode(DogMode.COME).ok


def test_jump_mode_queues_hop():
    dog = DogBehavior(HopController(SimMotionBus()))
    dog.set_mode(DogMode.JUMP)
    airborne = False
    for _ in range(300):
        st = dog.tick(0.01)
        if st.height_m > 0.02:
            airborne = True
            break
    assert airborne


def test_estop_blocks_modes():
    dog = DogBehavior(HopController(SimMotionBus()))
    dog.emergency_stop()
    r = dog.set_mode(DogMode.HEEL)
    assert not r.ok
    assert r.reason == "estopped"
