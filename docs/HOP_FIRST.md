# Hop-first program lock

**Wil 2026-11-19**

## Chassis

**One-leg Salto-class hopper only.** Wheeled bases rejected. Hard problem preferred.

## Goal order (strict)

1. **Hardware** — locked BOM with buy links: [`BOM.md`](BOM.md)  
2. **Mechanical build** — OpenSCAD kit [`../cad/`](../cad/) + motor plate after SKUs land  
3. **Stand / hop / balance** — gates G1→G4 in BOM  
4. **Later** — cam, 2 mics, speaker-ID, vision follow, sit-places (sensing backlog; not blocking)

## On-body control split

- **Teensy 4.1** — hop/balance (motors, IMU, encoders)  
- **ESP32-S3** — radio modem only  
- **amini** — later brain/remote; never inside 1 kHz loop for first hops  

## Mass

220–320 g hop-first. Sensor snout mounts reserved empty.

## Inspiration

Public UC Berkeley Salto / Salto-1P literature (SE + MA, reaction tail, thrusters later). No affiliation; original CAD.
