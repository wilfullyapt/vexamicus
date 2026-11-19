"""Vexamicus CLI."""

from __future__ import annotations

import argparse
import json
import sys

from vexamicus import __version__
from vexamicus.dog_fsm import DogBehavior
from vexamicus.follow import FollowPolicy, FollowTarget
from vexamicus.hop import HopController
from vexamicus.link import CommandMessage, TelemetryMessage, decode_message, encode_command
from vexamicus.modes import DogMode
from vexamicus.motion_bus import SimMotionBus, make_motion_bus
from vexamicus.safety import SafetyGate


def _build_dog(*, armed: bool = False) -> DogBehavior:
    bus = SimMotionBus(safety=SafetyGate(armed=armed))
    return DogBehavior(HopController(bus))


def _cmd_version(_: argparse.Namespace) -> int:
    print(__version__)
    return 0


def _cmd_sim_tick(args: argparse.Namespace) -> int:
    dog = _build_dog(armed=args.armed)
    if args.jump:
        dog.set_mode(DogMode.JUMP)
    elif args.mode:
        dog.set_mode(args.mode)
    last = None
    for _ in range(args.steps):
        last = dog.tick(args.dt)
    assert last is not None
    print(
        json.dumps(
            {
                "ok": True,
                "version": __version__,
                "steps": args.steps,
                "mode": dog.mode.value,
                "motion": last.as_dict(),
            }
        )
    )
    return 0


def _cmd_sim_jumps(args: argparse.Namespace) -> int:
    bus = SimMotionBus()
    hop = HopController(bus)
    metrics = hop.run_jumps(args.count, dt_s=args.dt)
    state = bus.read_state()
    print(
        json.dumps(
            {
                "ok": True,
                "version": __version__,
                "requested": args.count,
                "hops": metrics.hops,
                "peak_height_m": round(metrics.peak_height_m, 4),
                "last_flight_time_s": round(state.last_flight_time_s, 4),
                "phase": state.phase.value,
            }
        )
    )
    return 0 if metrics.hops >= args.count else 1


def _cmd_dog_status(args: argparse.Namespace) -> int:
    dog = _build_dog()
    if args.mode:
        dog.set_mode(args.mode)
    print(json.dumps({"ok": True, "version": __version__, **dog.status()}))
    return 0


def _cmd_dog_set(args: argparse.Namespace) -> int:
    dog = _build_dog()
    result = dog.set_mode(args.mode)
    print(
        json.dumps(
            {
                "ok": result.ok,
                "version": __version__,
                "mode": result.mode.value,
                "reason": result.reason,
                "status": dog.status(),
            }
        )
    )
    return 0 if result.ok else 1


def _cmd_follow_step(args: argparse.Namespace) -> int:
    policy = FollowPolicy(leash_m=args.leash)
    cmd = policy.step(
        DogMode(args.mode),
        FollowTarget(x_m=args.x, y_m=args.y, valid=not args.lost),
    )
    print(
        json.dumps(
            {
                "ok": True,
                "version": __version__,
                "forward_m_s": round(cmd.forward_m_s, 4),
                "yaw_rate_rad_s": round(cmd.yaw_rate_rad_s, 4),
                "lose_target": cmd.lose_target,
            }
        )
    )
    return 0


def _cmd_link_encode(args: argparse.Namespace) -> int:
    mode = DogMode(args.mode) if args.mode else None
    line = encode_command(CommandMessage(mode=mode, hop=args.hop, estop=args.estop, id=args.id))
    print(line)
    return 0


def _cmd_link_decode(args: argparse.Namespace) -> int:
    msg = decode_message(args.json)
    if hasattr(msg, "to_dict"):
        print(json.dumps({"ok": True, "message": msg.to_dict()}))
    return 0


def _cmd_backend_check(args: argparse.Namespace) -> int:
    try:
        bus = make_motion_bus(args.backend, armed=args.armed, allow_hw=args.allow_hw)
    except Exception as exc:  # noqa: BLE001 — CLI surface
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1
    state = bus.read_state()
    print(
        json.dumps(
            {
                "ok": True,
                "backend": args.backend,
                "type": type(bus).__name__,
                "state": state.as_dict(),
            }
        )
    )
    return 0


def _cmd_tel_sample(args: argparse.Namespace) -> int:
    dog = _build_dog(armed=args.armed)
    dog.set_mode(args.mode)
    for _ in range(args.steps):
        dog.tick(0.01)
    st = dog.hop.bus.read_state()
    tel = TelemetryMessage(
        mode=dog.mode,
        armed=args.armed,
        phase=st.phase.value,
        height_m=st.height_m,
        hop_count=st.hop_count,
    )
    print(json.dumps(tel.to_dict()))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="vexamicus", description="Vexamicus monoped body runtime")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("version", help="Print package version")
    sp.set_defaults(func=_cmd_version)

    sp = sub.add_parser("sim", help="Simulation commands")
    sim_sub = sp.add_subparsers(dest="sim_cmd", required=True)

    t = sim_sub.add_parser("tick", help="Tick sim N steps")
    t.add_argument("--steps", type=int, default=10)
    t.add_argument("--dt", type=float, default=0.01)
    t.add_argument("--jump", action="store_true")
    t.add_argument("--mode", default="")
    t.add_argument("--armed", action="store_true")
    t.set_defaults(func=_cmd_sim_tick)

    j = sim_sub.add_parser("jumps", help="Run N sequential hop cycles")
    j.add_argument("--count", type=int, default=3)
    j.add_argument("--dt", type=float, default=0.01)
    j.set_defaults(func=_cmd_sim_jumps)

    sp = sub.add_parser("dog", help="Dog mode FSM")
    dog_sub = sp.add_subparsers(dest="dog_cmd", required=True)
    ds = dog_sub.add_parser("status", help="Show dog + motion status")
    ds.add_argument("--mode", default="")
    ds.set_defaults(func=_cmd_dog_status)
    dset = dog_sub.add_parser("set", help="Set dog mode")
    dset.add_argument("mode", choices=[m.value for m in DogMode])
    dset.set_defaults(func=_cmd_dog_set)

    sp = sub.add_parser("follow", help="Follow policy (synthetic)")
    fsub = sp.add_subparsers(dest="follow_cmd", required=True)
    fs = fsub.add_parser("step", help="One follow policy step")
    fs.add_argument("--mode", default="heel", choices=[m.value for m in DogMode])
    fs.add_argument("--x", type=float, default=2.0)
    fs.add_argument("--y", type=float, default=0.0)
    fs.add_argument("--leash", type=float, default=1.5)
    fs.add_argument("--lost", action="store_true")
    fs.set_defaults(func=_cmd_follow_step)

    sp = sub.add_parser("link", help="Motion link schema v1")
    lsub = sp.add_subparsers(dest="link_cmd", required=True)
    le = lsub.add_parser("encode", help="Encode a command line")
    le.add_argument("--mode", default="")
    le.add_argument("--hop", action="store_true")
    le.add_argument("--estop", action="store_true")
    le.add_argument("--id", default="")
    le.set_defaults(func=_cmd_link_encode)
    ld = lsub.add_parser("decode", help="Decode a JSON message")
    ld.add_argument("json")
    ld.set_defaults(func=_cmd_link_decode)
    lt = lsub.add_parser("tel-sample", help="Emit sample telemetry after sim ticks")
    lt.add_argument("--mode", default="jump")
    lt.add_argument("--steps", type=int, default=30)
    lt.add_argument("--armed", action="store_true")
    lt.set_defaults(func=_cmd_tel_sample)

    sp = sub.add_parser("backend", help="Motion backend sanity")
    bsub = sp.add_subparsers(dest="backend_cmd", required=True)
    bc = bsub.add_parser("check", help="Construct backend")
    bc.add_argument("--backend", default="sim", choices=["sim", "hw"])
    bc.add_argument("--armed", action="store_true")
    bc.add_argument("--allow-hw", action="store_true")
    bc.set_defaults(func=_cmd_backend_check)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
