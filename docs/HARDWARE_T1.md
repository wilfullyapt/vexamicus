# Vexamicus T1 Hop Core — hardware lock

**Wil 2026-11-19:** one-leg hopper only · hardware → build → stand/hop/balance · sensors/voice later.

## Full locked BOM + buy links

**→ [BOM.md](BOM.md)** (authoritative)

## Stack (summary)

- **MCU:** Teensy 4.1 — [pjrc.com/store/teensy41.html](https://www.pjrc.com/store/teensy41.html)
- **Radio:** ESP32-S3 — [Adafruit 5364](https://www.adafruit.com/product/5364)
- **IMU:** ICM-42688-P — [SparkFun MikroE](https://www.sparkfun.com/mikroe-6dof-imu-14-click-sen-18783.html) · alt [LSM6DSOX](https://www.adafruit.com/product/4438)
- **Leg:** XING 2205 + 20 A BLHeli_S + ~25:1 gearbox + latex SEA
- **Pitch:** BLDC + printed reaction wheel ([cad/parts/tail_wheel.scad](../cad/parts/tail_wheel.scad))
- **Mass:** 220–320 g hop-first

## CAD models

**→ [MODELS.md](MODELS.md)** · tree https://github.com/wilfullyapt/vexamicus/tree/main/cad

## Gates

G1 hand-wind SEA · G2 tether hop · G3 pitch recover · G4 free hop
