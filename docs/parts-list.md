# InnoBots — WRO Future Engineers 2026 | Parts List

This inventory records the components supplied by the team. Quantities and exact variants are marked **TBC** where they have not yet been confirmed.

| No. | Component | Subsystem / role | Qty. | Details to confirm |
|---:|---|---|---|---|
| 1 | Raspberry Pi 5 | Main computing platform | TBC | RAM variant, cooling, storage, power supply |
| 2 | Raspberry Pi Camera Module 3 | Camera / visual perception | TBC | Standard or Wide variant; mounting and ribbon |
| 3 | D500 LiDAR | Distance sensing | TBC | Manufacturer, full model, interface, voltage, protocol |
| 4 | MG90S servo | Steering actuator | TBC | Supply voltage, torque, travel, model authenticity |
| 5 | 2S Li-ion battery | Main energy source | TBC | Capacity, discharge rating, cell configuration, connector |
| 6 | 2S BMS | Battery protection / balancing | TBC | Continuous and peak current ratings; protection features |
| 7 | XL4015 DC-DC converter | Voltage regulation | TBC | Input/output range, set voltage, continuous current, cooling |
| 8 | Arduino Pro Mini | Low-level microcontroller | TBC | 3.3 V or 5 V; 8 MHz or 16 MHz |
| 9 | DRV8833 motor driver | DC motor driver | TBC | Board version, current capability, motor supply voltage |
| 10 | Encoder | Motor feedback | TBC | Type, pulses per revolution, channels, output voltage |
| 11 | R260 DC motor | Drive motor | TBC | Exact variant, rated voltage, stall current, speed, gearbox |

## Subsystem overview

- **Computing and vision:** Raspberry Pi 5 and Camera Module 3.
- **Distance sensing:** D500 LiDAR.
- **Low-level control and feedback:** Arduino Pro Mini and encoder.
- **Drive and steering:** R260 DC motor, DRV8833 motor driver, and MG90S servo.
- **Power:** 2S Li-ion battery, 2S BMS, and XL4015 converter.

## Integration checks

1. Verify the 2S battery chemistry, cell configuration, voltage limits, BMS current rating, and connector polarity.
2. Confirm that the Pi 5 power rail can supply the required voltage and current under load. Do not assume the XL4015 module is suitable without checking its continuous-current and thermal capability.
3. Compare the R260 motor stall current with the DRV8833 module's current limits. Do not size the driver using no-load current alone.
4. Check the MG90S supply voltage and peak current. Do not power a servo from a microcontroller GPIO pin.
5. Raspberry Pi 5 GPIO uses 3.3 V logic and is not 5 V tolerant. Check interface compatibility and use suitable level shifting where required.
6. Confirm the full D500 LiDAR model and follow its datasheet for power, interface, and startup requirements.
7. Verify encoder pulses per revolution before using RPM calculations.

## Information still needed

- Quantity and ownership/purchase status for each component.
- Exact manufacturer and model variants.
- Battery capacity and discharge rating; BMS current rating.
- Motor rated voltage, stall current, speed, and gearbox details.
- Encoder pulses per revolution and signal type.
- Arduino Pro Mini voltage/clock version.
- Final power distribution and wiring diagram.

**Document status:** initial team-provided inventory. This list does not replace component datasheets, a verified wiring schematic, or electrical safety checks.
