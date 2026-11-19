# Vexamicus CAD (OpenSCAD)

Parametric **T1 hop-core** monoped kit. Original geometry (Salto-class proportions, not a Berkeley replica).

**BOM + buy links:** [docs/BOM.md](../docs/BOM.md)  
**Model index:** [docs/MODELS.md](../docs/MODELS.md)  
**GitHub tree:** https://github.com/wilfullyapt/vexamicus/tree/main/cad

## Layout

| Path | Role |
|------|------|
| `params.scad` | Global mm / SCALE |
| `vitamins.scad` | Holes, pockets |
| `parts/*.scad` | Printable parts (file invokes the part for STL export) |
| `assembly.scad` | Full preview |
| `export/` | Local STL/PNG (gitignored; regenerate) |

## Parts ↔ BOM

| Part | File | GitHub |
|------|------|--------|
| Body | `parts/body_core.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/body_core.scad) |
| SEA hub | `parts/sea_hub.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/sea_hub.scad) |
| Femur | `parts/femur.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/femur.scad) |
| Shin | `parts/shin.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/shin.scad) |
| Coupler | `parts/coupler.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/coupler.scad) |
| Foot | `parts/foot_toe.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/foot_toe.scad) |
| Tail wheel | `parts/tail_wheel.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/tail_wheel.scad) |
| Thruster boom (later) | `parts/thruster_boom.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/thruster_boom.scad) |
| Assembly | `assembly.scad` | [link](https://github.com/wilfullyapt/vexamicus/blob/main/cad/assembly.scad) |

## Export

```bash
cd cad
openscad -o export/assembly.png --imgsize=1280,800 \
  --camera=200,180,120,0,0,0,450 assembly.scad
for p in body_core sea_hub femur shin coupler foot_toe tail_wheel thruster_boom; do
  openscad -o export/${p}.stl parts/${p}.scad
done
```

## Print notes

- PETG (default) or ABS-CF  
- 0.2 mm layers, 4–6 walls, 40–60% gyroid on links  
- SEA hub denser (≈80%+)  
- M3 + 623 bearings at hip; brass inserts on tail wheel  

## Next CAD (after motor/gearbox in hand)

- `parts/motor_plate_leg.scad` — real bolt pattern  
- `parts/spring_cage.scad`  
- `parts/encoder_mount.scad`  
