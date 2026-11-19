# Vexamicus T1 Hop Core — Locked BOM

**Status:** LOCKED (Wil 2026-11-19)  
**Chassis:** one-leg SEA hopper only · **not wheeled**  
**Build order:** hardware → mechanical build → stand/hop/balance → later sensing software  
**Mass target:** 220–320 g hop-first  
**Version:** 1.0 · repo HEAD tracks this file  

Prices are approximate USD street; stock rotates — open the link and pick in-stock equivalent in the same class if needed.

---

## How to use this list

1. Buy **Priority A** first (everything needed for G1–G4 hop).  
2. Print parts from [`cad/`](../cad/) (model map below).  
3. After the exact leg motor + gearbox arrive, we cut a fitted `motor_plate` CAD revision.  
4. **Priority B** = T1.5 thrusters / sensor snout — do not block hop.

---

## Priority A — buy now (hop / stand / balance)

### Compute & sensors

| ID | Item | Qty | Locked pick | Buy |
|----|------|-----|-------------|-----|
| A1 | Control MCU | 1 | **Teensy 4.1** | [PJRC Teensy 4.1](https://www.pjrc.com/store/teensy41.html) |
| A2 | Radio modem | 1 | **ESP32-S3-DevKitC-1** | [Adafruit ESP32-S3-DevKitC-1](https://www.adafruit.com/product/5364) |
| A3 | IMU (primary) | 1 | **ICM-42688-P** breakout | [SparkFun / MikroE 6DOF IMU 14 Click (ICM-42688-P)](https://www.sparkfun.com/mikroe-6dof-imu-14-click-sen-18783.html) |
| A3b | IMU (alt if A3 OOS) | 1 | **LSM6DSOX** 6-DoF | [Adafruit LSM6DSOX](https://www.adafruit.com/product/4438) |
| A4 | Leg angle encoder | 2 | **AS5600** mag module + diametric magnet | [AS5600 modules (pack)](https://www.amazon.com/Magnetic-Encoder-Induction-Measurement-Precision/dp/B097QNG1CN) · search also “AS5600 encoder” |
| A5 | Logic regulator | 1 | **5 V ≥1 A** from 2S | [Pololu D24V10F5 5V 1A](https://www.pololu.com/product/2831) · or [D24V22F5 5V 2.5A](https://www.pololu.com/product/2858) |

### Leg drive (series-elastic)

| ID | Item | Qty | Locked pick | Buy |
|----|------|-----|-------------|-----|
| A6 | Leg BLDC | 1 | **2205 class ~2300 KV** (2–4S; we run **2S**) — Salto paper used Scorpion S-1804-1650; stock **XING 2205** is the locked available stand-in | [iFlight XING 2205 2300KV (Rotor Village)](https://rotorvillage.ca/iflight-xing-2205-2300kv-motor) · also search GetFPV / iFlight “XING 2205” |
| A7 | Leg ESC | 1–2 | **BLHeli_S / AM32 single 20 A** class, DShot | [DYS XSC-20A BLHeli_S (GetFPV)](https://www.getfpv.com/dys-xsc-20a-blheli-s-esc.html) · alt: any reputable **20 A BLHeli_S 2–4S** single ESC |
| A8 | Gear reduction | 1 | **~25:1** (20–30:1 OK) for ~5 mm / 12 mm-mount motors | [Rectified Robotics 22 mm gearbox](https://rectifiedrobotics.com/products/22mm-gearbox) · [22 mm planetary (Amazon class)](https://www.amazon.com/Diameter-Planetary-Reducer-Gearbox-Brushless/dp/B0DG8BNMWD) · [McMaster planetary gear boxes](https://www.mcmaster.com/products/planetary-gear-boxes/) |
| A9 | SEA spring | 1 pack | **Natural latex tubing** (torsion pack) | [McMaster latex tubing category](https://www.mcmaster.com/products/tubing/tubing-material~latex/) · start ~3–6 mm ID surgical/latex tube; tune on bench |
| A10 | SEA / crank hardware | lot | M3 axles, set screws, Loctite 243 | Hardware store / McMaster fasteners |

### Pitch (reaction wheel)

| ID | Item | Qty | Locked pick | Buy |
|----|------|-----|-------------|-----|
| A11 | Tail BLDC | 1 | **1404–1804** class or second **2205** if simpler logistics | Same shops as A6 — search “1404 4000KV” or use second XING 2205 lightly geared |
| A12 | Tail ESC | 1 | Same class as A7 (can share spare) | Same as A7 |
| A13 | Wheel mass | 8–16 | **Brass heat-set / threaded inserts** or M4 brass screws as rim weights | McMaster brass inserts · Amazon “M3 heat set inserts” |

### Power, structure, foot, bench

| ID | Item | Qty | Locked pick | Buy |
|----|------|-----|-------------|-----|
| A14 | Battery | 1–2 | **2S 350–500 mAh** 45–75C LiPo + XT30 | Search CNHL / Tattu / GNB “2S 450 mAh XT30” at GetFPV / RaceDayQuads / local hobby |
| A15 | Carbon tube | 1 m | **3 mm OD** carbon tube | [McMaster carbon fiber tubing](https://www.mcmaster.com/products/tubing/tubing-type~round/material~carbon-fiber/) · Amazon “3mm carbon fiber tube” |
| A16 | Bearings | 10 | **623ZZ** and/or **683ZZ** flanged | Amazon / McMaster “623ZZ bearing” |
| A17 | Foot rubber | 1 | High-µ rubber hemisphere / ball | McMaster rubber balls · or cut from superball / sorbothane pad |
| A18 | Filament | 1 kg | **PETG** (default) or ABS-CF | Prusament / Hatchbox PETG |
| A19 | Fasteners | lot | M2/M3 button head, nylock | McMaster |
| A20 | Tether line | 1 | Dyneema / heavy fishing line + swivel | Outdoor store |
| A21 | Foam pit | 1 | Gym mat / crash pad | Local |
| A22 | LiPo bag + charger | 1 | Balance charger 2S capable | Hobby store |
| A23 | Wire / connectors | lot | 22–28 AWG silicone, XT30 pigtails, header wire | Adafruit / Amazon |

**Est. Priority A cash:** ~$280–450 depending on gearbox and how many spares.

---

## Priority B — after G3/G4 (do not block hop)

| ID | Item | Notes | Buy / CAD |
|----|------|-------|-----------|
| B1 | Roll/yaw thrusters | 2× 8520 coreless + 31–40 mm props | Amazon “8520 coreless motor” |
| B2 | Cam snout | OV2640/UVC later | deferred |
| B3 | 2× MEMS mics | I2S pair later | deferred |
| B4 | Dock / Qi | sit-charge later | deferred |

---

## Explicit rejects

- Wheeled base as the robot  
- Pi 5 / Hailo on body  
- No spring (direct-drive-only leg)  
- Parallel-elastic latch mega-jumper as v1  
- Plastic tail gearbox as final  
- Cloud / amini inside the 1 kHz balance loop  

---

## Electrical (locked)

```
2S LiPo ─┬─ ESC_leg ── BLDC_leg ── gearbox ── latex SEA ── 4-bar leg
         ├─ ESC_tail ── BLDC_tail ── reaction wheel
         ├─ Pololu 5V ── Teensy 4.1 ── IMU + AS5600s + DShot
         └───────────── UART ── ESP32-S3 ── Wi-Fi/BLE (telemetry)
```

---

## CAD models in this repo (print these)

GitHub tree: https://github.com/wilfullyapt/vexamicus/tree/main/cad

| BOM role | OpenSCAD source | Export STL (local) | GitHub |
|----------|-----------------|--------------------|--------|
| Assembly preview | [`cad/assembly.scad`](../cad/assembly.scad) | `cad/export/assembly.stl` | [assembly.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/assembly.scad) |
| Body / battery / MCU tray | [`cad/parts/body_core.scad`](../cad/parts/body_core.scad) | `body_core.stl` | [body_core.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/body_core.scad) |
| Latex SEA hub + crank | [`cad/parts/sea_hub.scad`](../cad/parts/sea_hub.scad) | `sea_hub.stl` | [sea_hub.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/sea_hub.scad) |
| Femur link | [`cad/parts/femur.scad`](../cad/parts/femur.scad) | `femur.stl` | [femur.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/femur.scad) |
| Shin link | [`cad/parts/shin.scad`](../cad/parts/shin.scad) | `shin.stl` | [shin.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/shin.scad) |
| Coupler | [`cad/parts/coupler.scad`](../cad/parts/coupler.scad) | `coupler.stl` | [coupler.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/coupler.scad) |
| Foot + ankle rest | [`cad/parts/foot_toe.scad`](../cad/parts/foot_toe.scad) | `foot_toe.stl` | [foot_toe.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/foot_toe.scad) |
| Reaction wheel | [`cad/parts/tail_wheel.scad`](../cad/parts/tail_wheel.scad) | `tail_wheel.stl` | [tail_wheel.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/tail_wheel.scad) |
| Thruster boom (Priority B) | [`cad/parts/thruster_boom.scad`](../cad/parts/thruster_boom.scad) | `thruster_boom.stl` | [thruster_boom.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/parts/thruster_boom.scad) |
| Global dims | [`cad/params.scad`](../cad/params.scad) | — | [params.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/params.scad) |
| Shared holes | [`cad/vitamins.scad`](../cad/vitamins.scad) | — | [vitamins.scad](https://github.com/wilfullyapt/vexamicus/blob/main/cad/vitamins.scad) |
| CAD readme | [`cad/README.md`](../cad/README.md) | — | [cad/README](https://github.com/wilfullyapt/vexamicus/blob/main/cad/README.md) |

### Generate STLs

```bash
cd cad
for p in body_core sea_hub femur shin coupler foot_toe tail_wheel thruster_boom; do
  openscad -o "export/${p}.stl" "parts/${p}.scad"
done
openscad -o export/assembly.stl assembly.scad
```

### Still to add after motor/gearbox land (next CAD commit)

| Model | Purpose |
|-------|---------|
| `parts/motor_plate_leg.scad` | Bolt pattern for locked A6+A8 |
| `parts/spring_cage.scad` | Latex pack retention |
| `parts/encoder_mount.scad` | AS5600 + magnet alignment |
| `parts/teensy_tray.scad` | Optional discrete tray if body_core needs split print |

---

## Acceptance gates (hardware build)

| Gate | Meaning |
|------|---------|
| **G1** | Hand-wind SEA, free leg motion, stands on ankle rest |
| **G2** | ≥10 tethered powered hops, structure intact |
| **G3** | Reaction wheel recovers pitch in flight |
| **G4** | Untethered repeated hops on mat |

---

## Related docs

- [`HARDWARE_T1.md`](HARDWARE_T1.md) — short lock card  
- [`HOP_FIRST.md`](HOP_FIRST.md) — goal order & architecture  
- [`../DESIGN.md`](../DESIGN.md) — product design  
- Estate SoR: Reliquary `domains/shipyard/research/vexamicus-hardware-lock-monoped.md`
