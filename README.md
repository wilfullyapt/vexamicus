# Vexamicus

**Salto-class monoped body runtime** — sim-first MotionBus, hop cycle, dog mode FSM.  
Handheld brain/remote is **[mobile-ami](https://github.com/wilfullyapt/mobile-ami)** (`amini`), not this tree.

**Phase 0 (this release):** installable package + tests + CLI. **No real motors.** Hardware backends stay unarmed stubs.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check src tests && pytest -q
vexamicus version
vexamicus sim tick --steps 20
vexamicus dog set heel
vexamicus dog status
```

## What ships / what does not

| Ships in 0.1.0 | Does not ship yet |
|----------------|-------------------|
| `MotionBus` + **sim** backend | Real leg / reaction-wheel drivers |
| Sim hop metrics (height, flight time) | Measured outdoor agility |
| Dog modes + FSM | Live voice (lives on amini) |
| Motion-link JSON schema v1 | Chosen radio/serial bring-up |
| Safety arm flag (default **disarmed**) | BOM / printed chassis |

## Architecture

```
amini (brain)  --Motion link v1-->  Vexamicus (body)
                                    MotionBus → sim | hw*
```

\*hw refuses torque unless `armed: true` in config.

## License

MIT — see [LICENSE](LICENSE).  
Inspired by **public** UC Berkeley Salto / Salto-1P literature; **no** Berkeley affiliation or CAD.

## Estate

Vault map: Reliquary `domains/shipyard/maps/vexamicus.md` · ADR 0012.
