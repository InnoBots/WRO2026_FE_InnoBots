# InnoBots — WRO Future Engineers 2026 | Parts List & Torque Analysis

**Ibn Mandour High School · Morocco**

This document records the hardware inventory supplied by the InnoBots team and the motor data and preliminary torque calculation in the team's reference images. Quantities and unprovided specifications are marked **TBC** (to be confirmed). Values are not guessed.

## 1. Bill of materials

| No. | Component | Subsystem / role | Qty. | Details to confirm |
|---:|---|---|---|---|
| 1 | Raspberry Pi 5 | Main computing platform | TBC | RAM variant, cooling, storage, power supply |
| 2 | Raspberry Pi Camera Module 3 | Camera / visual perception | TBC | Standard or Wide variant; mounting and ribbon |
| 3 | D500 LiDAR | Distance sensing | TBC | Manufacturer, full model, interface, voltage, protocol |
| 4 | MG90S servo | Steering actuator | TBC | Supply voltage, torque, travel, peak current |
| 5 | 2S Li-ion battery | Main energy source | TBC | Capacity, discharge rating, cell configuration, connector |
| 6 | 2S BMS | Battery protection / balancing | TBC | Continuous and peak current ratings; protection features |
| 7 | XL4015 DC-DC converter | Voltage regulation | TBC | Input/output range, configured voltage, continuous current, cooling |
| 8 | Arduino Pro Mini | Low-level microcontroller | TBC | 3.3 V or 5 V; 8 MHz or 16 MHz |
| 9 | DRV8833 motor driver | DC motor driver | TBC | Exact board version, current capability, motor supply voltage |
| 10 | Encoder | Motor feedback | TBC | Type, pulses per revolution, channels, output voltage |
| 11 | **RE-260RA-2670 DC motor** | Drive motor | TBC | Motor reference image selects DC 3.0 V; team calculation uses 17:1 gearbox ratio |

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

These are the typical values visible in the supplied motor data image. Stall torque and stall current describe a stall condition and should not be treated as continuous operating values.

## 4. Team torque calculation

The following reproduces the calculation in the team's handwritten page.

### Given data

| Quantity | Symbol | Value |
|---|---:|---:|
| Robot mass | m | 0.630 kg |
| Wheel radius | R | 0.022 m |
| Rolling resistance coefficient | Crr | 0.01 |
| Gravity | g | 9.81 m/s² |
| Motor torque used in calculation | Tm | 1.70 mN·m |
| Gearbox ratio | i | 17:1 |
| Gearbox efficiency | ηg | 0.80 |

### Step 1 — Rolling resistance force

Frr = Crr × m × g

Frr = 0.01 × 0.630 × 9.81 = **0.0618 N**

### Step 2 — Minimum wheel torque to overcome rolling resistance

Tmin = Frr × R

Tmin = 0.0618 × 0.022 = 0.0013596 N·m ≈ **1.356 mN·m**

### Step 3 — Gearbox output torque using the team's stated motor torque

Tout = Tm × i × ηg

Tout = 1.70 × 17 × 0.80 = **23.12 mN·m**

### Step 4 — Torque ratio

S = Tout / Tmin

S = 23.12 / 1.356 ≈ **17.05**

**Conclusion from the handwritten calculation:** using its stated inputs, the estimated gearbox output torque is about 17.05 times the calculated torque needed to overcome rolling resistance on level ground.

### Important value to verify

There is a discrepancy between the two supplied references: the motor-data table lists **1.5 mN·m at maximum efficiency** for RE-260RA-2670 at 3.0 V, while the handwritten calculation uses **1.70 mN·m**. The images do not explain where 1.70 mN·m comes from, so the two values should not be presented as identical.

If the table's 1.5 mN·m maximum-efficiency torque is used instead, with the same 17:1 ratio and 80% gearbox efficiency:

Tout = 1.5 × 17 × 0.80 = **20.4 mN·m**

S = 20.4 / 1.356 ≈ **15.04**

Please verify the source and operating point for 1.70 mN·m before treating 17.05 as the final verified ratio.

### Scope and assumptions

This calculation considers rolling resistance only. It does not include acceleration, slopes, turning scrub, additional drivetrain losses, uneven surfaces, wheel slip, or transient loads. It assumes the stated motor torque is available at the motor shaft and that the 17:1 ratio applies to the drivetrain being analysed. It is a preliminary estimate, not proof of full-course performance. Confirm whether the motor and gearbox are integrated or separate, and verify the actual wheel/gear arrangement before using the result for final design decisions.

## 5. Integration checks

1. **Motor driver:** compare the DRV8833 module's current limits and thermal performance with the motor's listed **4.73 A stall current**. Do not assume the driver can safely supply stall current. Confirm the exact module datasheet and use appropriate current limiting and mechanical safeguards.
2. **Battery and power:** verify the 2S battery chemistry, cell configuration, voltage limits, BMS current rating, connector polarity, and protection arrangement.
3. **Raspberry Pi 5:** confirm that its power rail supplies the voltage and current required under load. Do not assume the XL4015 module is suitable without checking its actual continuous-current and thermal capability.
4. **Servo:** check the MG90S supply voltage and peak current. Do not power the servo directly from a microcontroller GPIO pin.
5. **Logic levels:** Raspberry Pi GPIO uses 3.3 V logic and is not 5 V tolerant. Verify signal compatibility between the Pi, Arduino, LiDAR, and encoder; use appropriate level shifting/interface circuitry where required.
6. **LiDAR:** confirm the full manufacturer/model identifier for “D500” and follow its datasheet for supply and communication requirements.
7. **Encoder:** confirm pulses per revolution and signal type before relying on RPM calculations.

## 6. Information still needed

- Quantity and ownership/purchase status for every component.
- Exact D500 LiDAR manufacturer/model and interface.
- Battery capacity, discharge rating, connector, and BMS current rating.
- XL4015 configured output voltage and verified continuous-current rating.
- Arduino Pro Mini voltage/clock version.
- DRV8833 board/module version and current rating.
- Encoder type, channel count, and pulses per revolution.
- Confirmation of gearbox type and ratio, and the source for the 1.70 mN·m motor torque value.
- Verified wiring diagram and measured system current.

**Document status:** Team-provided initial inventory plus preliminary torque analysis transcribed from the supplied images. Unknown quantities and specifications remain TBC. Verify component datasheets and measured robot performance before final submission.

---

*INNOBOTS · Ibn Mandour High School · Morocco · WRO Future Engineers 2026*
