# Vexamicus CAD (OpenSCAD)

Parametric **T0/T1** monoped kit. Geometry is **original** estate design inspired by published Salto-class proportions — not a Berkeley CAD replica.

## Layout

| Path | Role |
|------|------|
| `params.scad` | Global mm parameters / SCALE |
| `vitamins.scad` | Shared holes, pockets |
| `parts/*.scad` | Printable parts (each file ends with the part for STL export) |
| `assembly.scad` | Full preview pose |
| `export/` | Generated STL / PNG |

## Parts

- `body_core` — battery bay, MCU shelf, hip bearings, tail bore  
- `sea_hub` — latex torsion SEA + crank  
- `femur`, `shin`, `coupler` — T1 4-bar leg links  
- `foot_toe` — rubber seat + crouch ankle pads  
- `tail_wheel` — reaction wheel with brass-insert pockets  
- `thruster_boom` — optional T2 roll/yaw mounts  

## Export

```bash
cd cad
# preview PNG
openscad -o export/assembly.png --imgsize=1280,800 \
  --camera=200,180,120,0,0,0,450 assembly.scad

# STLs
for p in body_core sea_hub femur shin coupler foot_toe tail_wheel thruster_boom; do
  openscad -o export/${p}.stl parts/${p}.scad
done
```

## Print notes (starting point)

- Material: PETG or ABS-CF for structure; wheel can be PETG + brass inserts  
- Layer 0.2 mm, 4–6 walls, 40–60% gyroid on links  
- SEA hub: solid-ish (80%+) around spring slots  
- Post: M3 bolts, 623 bearings at hip, heat-set inserts where marked  

## Next CAD

- Exploded BOM annotations  
- Exact gearbox adapter once motor is purchased  
- T3 multi-bar MA leg (separate module) after T1 hops  
