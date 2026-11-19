"""CLI smoke tests."""

import json

from vexamicus import __version__
from vexamicus.cli import main


def test_version(capsys):
    assert main(["version"]) == 0
    assert capsys.readouterr().out.strip() == __version__


def test_sim_tick_json(capsys):
    assert main(["sim", "tick", "--steps", "5", "--jump"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["ok"] is True
    assert data["motion"]["hop_count"] >= 1


def test_dog_status(capsys):
    assert main(["dog", "status"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["mode"] == "stop"


def test_dog_set_heel(capsys):
    assert main(["dog", "set", "heel"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["ok"] is True
    assert data["mode"] == "heel"


def test_sim_jumps(capsys):
    assert main(["sim", "jumps", "--count", "2"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["hops"] >= 2


def test_link_encode_decode(capsys):
    assert main(["link", "encode", "--mode", "come", "--id", "x"]) == 0
    line = capsys.readouterr().out.strip()
    assert main(["link", "decode", line]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data["message"]["mode"] == "come"
