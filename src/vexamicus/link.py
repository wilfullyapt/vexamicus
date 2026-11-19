"""Motion link schema v1 — JSON messages between brain and body."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from vexamicus.modes import DogMode

SCHEMA_VERSION = 1


class LinkError(ValueError):
    """Invalid link payload."""


@dataclass(frozen=True)
class CommandMessage:
    mode: DogMode | None = None
    hop: bool = False
    estop: bool = False
    id: str = ""

    def to_dict(self) -> dict[str, Any]:
        d: dict[str, Any] = {
            "v": SCHEMA_VERSION,
            "kind": "cmd",
            "hop": self.hop,
            "estop": self.estop,
        }
        if self.id:
            d["id"] = self.id
        if self.mode is not None:
            d["mode"] = self.mode.value
        return d


@dataclass(frozen=True)
class TelemetryMessage:
    mode: DogMode
    armed: bool
    phase: str
    height_m: float
    hop_count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "v": SCHEMA_VERSION,
            "kind": "tel",
            "mode": self.mode.value,
            "armed": self.armed,
            "phase": self.phase,
            "height_m": self.height_m,
            "hop_count": self.hop_count,
        }


def encode_command(msg: CommandMessage) -> str:
    return json.dumps(msg.to_dict(), separators=(",", ":"))


def encode_telemetry(msg: TelemetryMessage) -> str:
    return json.dumps(msg.to_dict(), separators=(",", ":"))


def decode_message(raw: str | bytes | dict[str, Any]) -> CommandMessage | TelemetryMessage:
    if isinstance(raw, dict):
        data = raw
    else:
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8")
        data = json.loads(raw)
    if not isinstance(data, dict):
        raise LinkError("message must be a JSON object")
    ver = data.get("v")
    if ver != SCHEMA_VERSION:
        raise LinkError(f"unsupported schema version: {ver!r}")
    kind = data.get("kind")
    if kind == "cmd":
        mode_raw = data.get("mode")
        mode = DogMode(mode_raw) if mode_raw is not None else None
        return CommandMessage(
            mode=mode,
            hop=bool(data.get("hop", False)),
            estop=bool(data.get("estop", False)),
            id=str(data.get("id", "") or ""),
        )
    if kind == "tel":
        return TelemetryMessage(
            mode=DogMode(str(data["mode"])),
            armed=bool(data.get("armed", False)),
            phase=str(data.get("phase", "idle")),
            height_m=float(data.get("height_m", 0.0)),
            hop_count=int(data.get("hop_count", 0)),
        )
    raise LinkError(f"unknown kind: {kind!r}")
