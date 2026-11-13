# InnoBots — WRO Future Engineers 2026 | Parts List & Torque Analysis

**Ibn Mandour High School · Morocco**

This document summarizes the robot's main hardware, the motor data shown in the team's reference image, and the team's preliminary rolling-resistance torque calculation.

## 1. Bill of materials

| No. | Component | Subsystem / role | Recorded specification |
|---:|---|---|---|
| 1 | Raspberry Pi 5 | Main computing platform | Main controller for high-level processing |
| 2 | Raspberry Pi Camera Module 3 | Visual perception | Camera module |
| 3 | D500 LiDAR | Distance sensing | LiDAR distance sensor |
| 4 | MG90S servo | Steering actuator | Micro servo |
| 5 | 2S Li-ion battery | Main energy source | 2-cell series battery pack |
| 6 | 2S BMS | Battery protection | 2-cell battery management system |
| 7 | XL4015 DC-DC converter | Voltage regulation | Adjustable DC-DC converter |
| 8 | Arduino Pro Mini | Low-level control | Microcontroller board |
| 9 | DRV8833 motor driver | DC motor driver | Dual H-bridge motor driver |
| 10 | Encoder | Motor feedback | Rotational feedback sensor |
| 11 | RE-260RA-2670 DC motor | Drive motor | 3.0 V reference motor; 17:1 gearbox ratio used in team calculation |

## 2. Subsystem overview

- **Computing and vision:** Raspberry Pi 5 and Raspberry Pi Camera Module 3.
- **Distance sensing:** D500 LiDAR.
- **Low-level control and feedback:** Arduino Pro Mini and encoder.
- **Drive and steering:** RE-260RA-2670 DC motor, DRV8833 motor driver, and MG90S servo.
- **Power:** 2S Li-ion battery, 2S BMS, and XL4015 DC-DC converter.

## 3. Motor identification — RE-260RA-2670

The motor-data image supplied by the team identifies the selected motor as **RE-260RA-2670 at DC 3.0 V**. The image gives the following typical data:

| Parameter | Value | Operating point |
|---|---:|---|
| Operating voltage range | DC 1.5–6.0 V | Model range shown in table |
| Nominal voltage selected | DC 3.0 V | Team's selected row |
| No-load speed | 12,300 r/min | No load |
| No-load current | 0.20 A | No load |
| Speed at maximum efficiency | 10,200 r/min | Maximum-efficiency point |
| Current at maximum efficiency | 0.97 A | Maximum-efficiency point |
| Torque at maximum efficiency | **1.5 mN·m** | Maximum-efficiency point |
| Output power at maximum efficiency | 1.6 W | Maximum-efficiency point |
| Stall torque | 8.77 mN·m | Stall condition |
| Stall current | 4.73 A | Stall condition |

Stall torque and stall current describe a stall condition and are not continuous operating values.

## 4. Team torque calculation

The following reproduces the calculation in the team's handwritten reference.

### Given data

| Quantity | Symbol | Value |
|---|---:|---:|
| Robot mass | m | 0.630 kg |
| Wheel radius | R | 0.022 m |
| Rolling resistance coefficient | Crr | 0.01 |
| Gravity | g | 9.81 m/s² |
| Motor torque used in handwritten calculation | Tm | 1.70 mN·m |
| Gearbox ratio | i | 17:1 |
| Gearbox efficiency | ηg | 0.80 |

### Step 1 — Rolling resistance force

Frr = Crr × m × g

Frr = 0.01 × 0.630 × 9.81 = **0.0618 N**

### Step 2 — Minimum wheel torque to overcome rolling resistance

Tmin = Frr × R

Tmin = 0.0618 × 0.022 = 0.0013596 N·m ≈ **1.356 mN·m**

### Step 3 — Gearbox output torque using the handwritten motor torque

Tout = Tm × i × ηg

Tout = 1.70 × 17 × 0.80 = **23.12 mN·m**

### Step 4 — Torque ratio

S = Tout / Tmin

S = 23.12 / 1.356 ≈ **17.05**

Using the handwritten calculation's stated inputs, the estimated gearbox output torque is about 17.05 times the calculated torque needed to overcome rolling resistance on level ground.

### Motor-table comparison

The motor-data table lists **1.5 mN·m at maximum efficiency**, while the handwritten calculation uses **1.70 mN·m**. These are distinct reference values.

Using the motor-table value with the same 17:1 ratio and 80% gearbox-efficiency assumption:

Tout = 1.5 × 17 × 0.80 = **20.4 mN·m**

S = 20.4 / 1.356 ≈ **15.04**

The calculation therefore gives a torque ratio of approximately **15.04** when the motor-table torque is used, or **17.05** with the torque value written in the handwritten calculation.

### Scope of the calculation

This calculation considers rolling resistance only. It does not include acceleration, slopes, turning scrub, additional drivetrain losses, uneven surfaces, wheel slip, or transient loads. It is a theoretical estimate for level-ground motion rather than a measurement of full-course performance.

## 5. Electrical and mechanical integration context

The motor's listed stall current is **4.73 A**. Motor-driver current limits and thermal behavior are important when selecting the drive electronics. The 2S battery architecture, voltage conversion, servo supply, and signal interfaces are described in [Elec/POWER_MANAGEMENT.md](../Elec/POWER_MANAGEMENT.md).

The Raspberry Pi uses 3.3 V GPIO logic. Signal connections to other controllers and sensors must respect their voltage limits. A servo should be powered from a suitable supply rather than directly from a microcontroller GPIO pin.

---

*INNOBOTS · Ibn Mandour High School · Morocco · WRO Future Engineers 2026*
