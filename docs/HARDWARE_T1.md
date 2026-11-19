# Vexamicus T1 Hop Core — hardware lock

**Wil 2026-11-19:** one-leg hopper only · hardware → build → stand/hop/balance · sensors/voice later.

Full estate write-up: Reliquary `domains/shipyard/research/vexamicus-hardware-lock-monoped.md`.

## Locked stack

- **MCU:** Teensy 4.1 (balance/hop loop)
- **Radio:** ESP32-S3 modem only
- **IMU:** ICM-42688-P SPI
- **Leg:** BLDC 1806–2205 @ 1500–1800 KV + 15–20 A ESC + **~25:1** gear + **latex torsion SEA**
- **Pitch:** BLDC + reaction wheel (brass mass)
- **Power:** 2S 350–500 mAh
- **Frame:** PETG/ABS-CF + 3 mm carbon + rubber toe
- **Mass:** 220–320 g hop-first
- **Not now:** wheels, thrusters (until pitch works), Pi on body, cam/mics populated

## Gates

- G1 hand-wind SEA · G2 tether hop · G3 pitch recover · G4 free hop

## CAD

See `/cad` — next adapter plate after exact motor SKU lands.
