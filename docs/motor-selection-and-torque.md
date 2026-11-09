# Motor selection & torque analysis

The drive motor documented for this build is the **RE-260RA-2670**, selected at **DC 3.0 V**. This page records the values visible in the motor data supplied by the team and the team's handwritten torque calculation. It keeps the reference data and the calculation inputs separate so the engineering record remains traceable.

## Motor data — RE-260RA-2670 at 3.0 V

| Parameter | Typical value |
|---|---:|
| Operating range | DC 1.5–6.0 V |
| Nominal voltage shown | DC 3.0 V |
| No-load speed | 12,300 r/min |
| No-load current | 0.20 A |
| Speed at maximum efficiency | 10,200 r/min |
| Current at maximum efficiency | 0.97 A |
| Torque at maximum efficiency | 1.5 mN·m |
| Torque at maximum efficiency | 15.2 g·cm |
| Output power at maximum efficiency | 1.6 W |
| Stall torque | 8.77 mN·m |
| Stall torque | 90 g·cm |
| Stall current | 4.73 A |

These are typical reference values from the supplied motor-data table, not measurements taken on our robot.

## Torque calculation supplied by the team

### Given values

| Quantity | Symbol | Value |
|---|---:|---:|
| Robot mass | m | 0.630 kg |
| Wheel radius | R | 0.022 m |
| Rolling resistance coefficient | Crr | 0.01 |
| Gravitational acceleration | g | 9.81 m/s² |
| Motor torque used in calculation | Tm | 1.70 mN·m |
| Gearbox ratio | i | 17:1 |
| Gearbox efficiency | ηg | 0.80 |

### 1. Rolling resistance force

Frr = Crr × m × g

Frr = 0.01 × 0.630 × 9.81 = **0.0618 N**

### 2. Minimum wheel torque to overcome rolling resistance

Tmin = Frr × R

Tmin = 0.0618 × 0.022 = **0.001356 N·m = 1.356 mN·m**

### 3. Gearbox output torque

Using the motor torque value written in the team's calculation:

Tout = Tm × i × ηg

Tout = 1.70 × 17 × 0.80 = **23.12 mN·m**

### 4. Torque ratio

S = Tout / Tmin

S = 23.12 / 1.356 ≈ **17.05**

The team's calculation therefore reports gearbox output torque approximately 17.05 times the calculated torque needed to overcome rolling resistance on level ground.

## Engineering note — value to verify

The motor data table supplied with the project lists **1.5 mN·m** at maximum efficiency for the RE-260RA-2670 at 3.0 V. The handwritten calculation instead uses **1.70 mN·m**. The sources do not explain this difference, so we are keeping both values visible rather than silently replacing one.

If 1.5 mN·m is used with the same 17:1 ratio and 80% gearbox efficiency:

Tout = 1.5 × 17 × 0.80 = **20.4 mN·m**

S = 20.4 / 1.356 ≈ **15.04**

The team should confirm the source and operating point for 1.70 mN·m before presenting 17.05 as the final verified ratio.

## What this calculation does — and does not — establish

This is a preliminary check against rolling resistance on level ground. It does not by itself prove the robot has enough torque for acceleration, slopes, turning, wheel slip, uneven surfaces, or transient loads. The final design review should also verify the motor's operating voltage, actual gearbox arrangement, drivetrain losses, and measured performance on the assembled robot.

The motor table lists a **4.73 A stall current**. The exact DRV8833 module and its current/thermal limits must be checked against the motor and operating conditions before the drive system is powered under load.

---

*InnoBots · WRO Future Engineers 2026 · Ibn Mandour High School, Morocco*
