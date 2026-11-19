# Vexamicus — DESIGN

**Product:** Salto-class monoped companion body  
**Phase:** 0 — contracts + sim  
**Version:** 0.1.0  
**Brain/remote:** mobile-ami (`amini`) — separate repo  
**Hub Hermes profile:** none  
**Visibility:** public MIT

## Thesis

Body ≠ brain. Vexamicus owns hop control, on-body safety, and MotionBus backends.  
mobile-ami owns voice, high-level dog UX, and the link **client**.

North-star program (phased gates, not one PR):

| Lane | Meaning |
|------|---------|
| L1 Jump | Hop / aerial attitude |
| L2 Follow | Owner envelope while/between hops |
| L3 Dog cmds | sit / stay / come / heel / jump / stop / free / orbit |

## MotionBus

Abstract actuator surface:

- `set_leg_extension(ratio 0..1)`
- `set_reaction_wheel_torque(nm)` (sim units)
- `estop()`
- `read_state() → MotionState`

**SimMotionBus** is the default CI/desk backend.  
**HwMotionBus** exists as a refuse-stub until real drivers land; construction requires `allow_hw=True` and still starts **disarmed**.

## Hop controller (sim)

Phase-0 hop is a **planar energy toy**, not a validated plant model:

1. Stance compresses a virtual spring.  
2. Extension releases impulse → vertical velocity.  
3. Flight integrates under gravity until touchdown.  
4. Metrics: peak height (m), flight time (s), hop count.

Inspired by published monoped hopping control ideas (series-elastic stance, aerial attitude). **Not** a copy of Berkeley CAD/firmware.

## Dog FSM

Modes: `stop`, `sit`, `stay`, `come`, `heel`, `jump`, `orbit`, `free`.

- Illegal transitions rejected with reason.  
- `jump` queues a single hop request on the hop controller when armed **or** always allowed in pure sim tick path via `force_sim`.  
- `stop` / e-stop clears motion commands.

## Motion link schema v1

JSON lines (UTF-8), one object per message.

**Brain → body (`cmd`):**

```json
{"v":1,"kind":"cmd","id":"…","mode":"heel","hop":false,"estop":false}
```

**Body → brain (`tel`):**

```json
{"v":1,"kind":"tel","mode":"heel","armed":false,"phase":"flight","height_m":0.12,"hop_count":3}
```

Unknown `v` → reject. amini will speak this schema later; phase 0 only encodes/decodes here.

## Safety

| Rule | Behavior |
|------|----------|
| Default | `armed=false` |
| Real hw path | Refuse if not armed |
| E-stop | Immediate zero commands; mode → `stop` |
| CI | Never imports hardware SDKs |

## Non-goals (phase 0)

- Real BOM / ASSEMBLY parts list (open until MCU vs SBC lock)  
- ROS2 runtime  
- Vision person-follow weights  
- Claiming Salto agility numbers  

## References (public)

- UC Berkeley Biomimetic Millisystems Lab — Salto / Salto-1P hopping robots (public papers and EECS writeups)  
- robotsguide.com/robots/salto  
- Estate research: Salto FB reel intake (video id 4200211160111461)

## Next phases

1. Freeze link schema + lose-target / e-stop behaviors in longer sims  
2. Body computer bring-up + IMU  
3. Measured bench hop with arming discipline  
