"""Motion link schema tests."""

import pytest

from vexamicus.link import (
    SCHEMA_VERSION,
    CommandMessage,
    LinkError,
    TelemetryMessage,
    decode_message,
    encode_command,
    encode_telemetry,
)
from vexamicus.modes import DogMode


def test_roundtrip_cmd():
    raw = encode_command(CommandMessage(mode=DogMode.HEEL, hop=False, id="a1"))
    msg = decode_message(raw)
    assert isinstance(msg, CommandMessage)
    assert msg.mode is DogMode.HEEL
    assert msg.id == "a1"


def test_roundtrip_tel():
    raw = encode_telemetry(
        TelemetryMessage(
            mode=DogMode.JUMP,
            armed=False,
            phase="flight",
            height_m=0.2,
            hop_count=2,
        )
    )
    msg = decode_message(raw)
    assert isinstance(msg, TelemetryMessage)
    assert msg.hop_count == 2
    assert msg.mode is DogMode.JUMP


def test_bad_version():
    with pytest.raises(LinkError):
        decode_message({"v": SCHEMA_VERSION + 1, "kind": "cmd"})
