# Vexamicus — DESIGN

**Product:** One-leg Salto-class hopper (monoped only)  
**Phase:** 0 software sim + **T1 hardware BOM locked**  
**Version:** 0.1.0 + docs BOM 1.0  
**Brain/remote:** mobile-ami (`amini`) — separate repo · **after** hop/balance  
**Hub Hermes profile:** none  
**Visibility:** public MIT  

## Thesis

Body ≠ brain. Vexamicus owns hop control, on-body safety, MotionBus, and (T1) physical monoped.  
mobile-ami owns later voice / who-may UX and link client.

### Goal order (locked)

1. Hardware BOM — see [`docs/BOM.md`](docs/BOM.md)  
2. Mechanical build — [`cad/`](cad/)  
3. Stand / hop / balance (G1–G4)  
4. Later software: follow, dog voice, sit-places, cam+2 mics  

## MotionBus

- `set_leg_extension(ratio 0..1)`
- `set_reaction_wheel_torque(nm)` (sim units)
- `estop()`
- `read_state() → MotionState`

**SimMotionBus** — default CI.  
**HwMotionBus** — refuse-stub until real drivers; needs `allow_hw=True` + armed.

## Hardware (T1)

| Role | Pick |
|------|------|
| Hop MCU | Teensy 4.1 |
| Modem | ESP32-S3 |
| IMU | ICM-42688-P (LSM6DSOX alt) |
| Leg | BLDC 2205 + ~25:1 + latex SEA + 4-bar |
| Pitch | Reaction wheel |
| Power | 2S 350–500 mAh |

Buy links + CAD mapping: **`docs/BOM.md`**.

## CAD

Parametric kit under `cad/` — index in `docs/MODELS.md`.

- T1 leg: 4-bar + latex torsion SEA (not a Salto 8-bar clone)  
- Attitude: reaction wheel; thruster booms optional after G3  

## Dog FSM / link v1

Modes and JSON link schema remain for **later** amini integration; hop firmware path is Teensy-first.

## Safety

Default `armed=false`. CI never loads motor SDKs. Bench tether required until G4.

## Non-goals (near term)

- Wheeled chassis  
- Cam/mics populated before G4  
- Voice/follow software before balance  
- Pi on body  
- Claiming Salto leap meters day one  

## References

- Haldane / Yim / Fearing Salto-1P papers  
- Plecnik SE+MA leg design paper  
- robotsguide.com/robots/salto  
