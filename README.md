# Vexamicus

**One-leg Salto-class hopper** — public MIT. **Not wheeled.**  
Later brain/remote: [mobile-ami](https://github.com/wilfullyapt/mobile-ami) (`amini`).

## Hop-first lock (Wil 2026-11-19)

1. **Hardware BOM** (buy links)  
2. **Mechanical build** (OpenSCAD)  
3. **Stand / hop / balance**  
4. **Later:** voice, who-may, vision follow, sit-places  

### Start here

| Doc | What |
|-----|------|
| **[docs/BOM.md](docs/BOM.md)** | **Locked BOM + buy links + CAD model links** |
| [docs/MODELS.md](docs/MODELS.md) | OpenSCAD → part map |
| [docs/HOP_FIRST.md](docs/HOP_FIRST.md) | Goal order |
| [docs/HARDWARE_T1.md](docs/HARDWARE_T1.md) | Short hardware card |
| [DESIGN.md](DESIGN.md) | MotionBus / software architecture |
| [cad/](cad/) | Printable OpenSCAD kit |

**CAD on GitHub:** https://github.com/wilfullyapt/vexamicus/tree/main/cad

## Software sim (phase 0 — already shipped)

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
ruff check src tests && pytest -q
vexamicus version
vexamicus sim jumps --count 3
vexamicus dog set heel
```

## Print CAD

```bash
cd cad
for p in body_core sea_hub femur shin coupler foot_toe tail_wheel; do
  openscad -o "export/${p}.stl" "parts/${p}.scad"
done
openscad -o export/assembly.stl assembly.scad
```

## Architecture

```
amini (later brain)  --link-->  Teensy 4.1 hop loop + ESP32 modem
                                MotionBus → sim | hw
```

## License

MIT — [LICENSE](LICENSE).  
Inspired by public UC Berkeley Salto / Salto-1P literature; **no** affiliation or copied CAD.
