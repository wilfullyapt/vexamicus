"""Follow policy tests."""

from vexamicus.follow import FollowPolicy, FollowTarget
from vexamicus.modes import DogMode


def test_lost_target():
    p = FollowPolicy()
    cmd = p.step(DogMode.HEEL, FollowTarget(valid=False))
    assert cmd.lose_target


def test_inside_leash_heel_holds():
    p = FollowPolicy(leash_m=1.5)
    cmd = p.step(DogMode.HEEL, FollowTarget(x_m=0.5, y_m=0.0))
    assert cmd.forward_m_s == 0.0


def test_far_target_moves():
    p = FollowPolicy(leash_m=1.0, max_speed_m_s=1.0)
    cmd = p.step(DogMode.COME, FollowTarget(x_m=3.0, y_m=0.0))
    assert cmd.forward_m_s > 0.0
