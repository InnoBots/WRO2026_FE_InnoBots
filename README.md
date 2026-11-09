# InnoBots — WRO Future Engineers 2026

<p align="center">
  <strong>Autonomous Robotics • Mechanical Engineering • Embedded Systems • Competition Documentation</strong>
</p>

<p align="center">
  <img src="t-photos/Team_photo.jpg" alt="InnoBots team" width="620">
</p>

Welcome to the official engineering repository of **InnoBots**, a team from Ibn Mandour High School in Morocco, documenting its work for the **World Robot Olympiad (WRO) Future Engineers 2026** competition.

This repository is intended to be the technical record of the project: the robot's mechanical design, electrical and power architecture, embedded software, testing process, design decisions, and the files needed to understand and reproduce the system. It is being developed as a living engineering document. Sections marked **To be completed** identify information or evidence that still needs to be added; they are not claims that a component or test has already been completed.

---

## Contents

- [Project at a glance](#project-at-a-glance)
- [The team](#the-team)
- [Robot overview](#robot-overview)
- [Repository structure](#repository-structure)
- [1. Mobility and mechanical design](#1-mobility-and-mechanical-design)
- [2. Electrical, power, and sensor architecture](#2-electrical-power-and-sensor-architecture)
- [3. Software architecture](#3-software-architecture)
- [4. Obstacle strategy and autonomous behaviour](#4-obstacle-strategy-and-autonomous-behaviour)
- [5. Systems engineering and design decisions](#5-systems-engineering-and-design-decisions)
- [Testing, calibration, and iteration](#testing-calibration-and-iteration)
- [Reproducing the project](#reproducing-the-project)
- [Current implementation status and next steps](#current-implementation-status-and-next-steps)
- [Acknowledgements and project information](#acknowledgements-and-project-information)

---

## Project at a glance

| Item | Current repository information |
|---|---|
| Team | InnoBots |
| Competition | World Robot Olympiad — Future Engineers |
| Project season | 2026 |
| School | Ibn Mandour High School |
| Country | Morocco |
| Main firmware language | Arduino C++ |
| Firmware location | [Code/](Code/) |
| Mechanical documentation | [Mech/](Mech/) |
| Electrical documentation | [Elec/](Elec/) |
| Team photographs | [t-photos/](t-photos/) |
| Robot photographs / videos | [v-photos/](v-photos/) |

The project combines mechanical construction, motor control, embedded programming, electrical integration, and autonomous-robotics problem solving. The repository currently contains an Arduino-style firmware foundation with separate source and header files for motor control, steering, and UART communication. The mechanical and electrical folders are reserved for the supporting design files and diagrams.

## The team

InnoBots is the team behind this WRO Future Engineers project. The team is responsible for researching, designing, building, programming, testing, and documenting the robot.

The team photograph is stored in `t-photos/Team_photo.jpg`. Individual member names, roles, and a short description of each member's engineering contribution should be added here once confirmed by the team.

**Team members and responsibilities — To be completed**

| Team member | Main responsibility | Contributions |
|---|---|---|
| To be completed | Mechanical design | CAD, chassis, steering and assembly |
| To be completed | Electronics | Power distribution, wiring and sensors |
| To be completed | Programming | Embedded firmware, control and testing |

---

## Robot overview

The goal of the project is to develop a robot capable of completing the WRO Future Engineers challenges while operating reliably and consistently. The design must bring together the mechanical platform, actuators, electronics, sensing, and software as one integrated system.

The current public repository does not yet contain enough verified information to publish final robot dimensions, a complete bill of materials, the exact controller board, the full sensor list, or measured performance figures. Those details will be added when confirmed from the actual build and its documentation.

### Robot media

- Team photographs: [t-photos/](t-photos/)
- Robot photographs and videos: [v-photos/](v-photos/)
- Mechanical files: [Mech/](Mech/)
- Electrical files: [Elec/](Elec/)

**Robot overview images, front / rear / left / right / top / bottom — To be added.**

A useful photo set should show the complete robot from multiple angles, the steering and drive mechanism, the electronics mounting, the battery location, and the sensor positions. Include captions so that another team can identify each subsystem.

---

## Repository structure

The repository is organized by engineering discipline so that readers can find the relevant implementation and supporting evidence.

```text
WRO2026_FE_InnoBots/
├── README.md
├── Code/
│   ├── main.ino
│   ├── motor.cpp
│   ├── motor.h
│   ├── sterring.cpp
│   ├── sterring.h
│   ├── uart.cpp
│   ├── uart.h
│   ├── power.cpp
│   └── power.h
├── Elec/
│   └── (electrical diagrams and component documentation)
├── Mech/
│   └── (CAD, drawings, and mechanical documentation)
├── t-photos/
│   └── (team photographs)
└── v-photos/
    └── (robot photographs and videos)
```

The file names shown above reflect the current firmware files. The `power.cpp` and `power.h` files are currently empty placeholders. The `Elec/` and `Mech/` folders need their final diagrams, CAD exports, and explanatory documents added.

---

## 1. Mobility and mechanical design

The mobility system determines how the robot moves, turns, maintains stability, and interacts with the competition field. Mechanical decisions should be explained in terms of the requirements they satisfy rather than presented only as a list of parts.

### Chassis and mechanical layout

**To be completed from the physical robot and CAD assembly:**

- Chassis material, construction method, and overall layout.
- Robot length, width, height, and mass.
- Position of the drive system, steering system, battery, controller, and sensors.
- Wheel type, diameter, spacing, and ground clearance.
- How the design protects electronics and keeps components securely mounted.
- How the layout supports access for maintenance and battery replacement.

Add dimensioned drawings and clear photographs to `Mech/`. If CAD is available, include the native project files where possible, plus neutral exchange formats such as STEP and printable STL files when relevant.

### Drive and steering

The firmware currently separates motor control from steering control:

- `Code/motor.cpp` and `Code/motor.h` contain the drive-motor control interface.
- `Code/sterring.cpp` and `Code/sterring.h` contain a servo-based steering interface.

The steering source includes the Arduino Servo library and defines a servo output pin. The current implementation exposes `Init()` and `setAngle(int angle)`; the PID-related functions are present as interfaces but are not yet implemented as a complete steering controller.

**Mechanical explanation to add:** identify the actual motor and steering mechanism, explain why they were selected, describe the linkage geometry and steering range, and include photographs or CAD views of the mechanism.

### Torque, speed, and mechanical trade-offs

A reproducible design should show how the required wheel force and speed were estimated. Add the actual robot mass, wheel radius, target speed, expected acceleration, surface assumptions, and motor/gearbox specifications before publishing numerical conclusions.

A useful calculation record should include:

1. Required travel speed and wheel rotational speed.
2. Estimated rolling resistance and acceleration demand.
3. Required wheel torque, including the chosen safety margin.
4. Gear ratio and drivetrain efficiency, where applicable.
5. Comparison between calculated requirements and the selected motor's specifications.

**No torque, speed, or drivetrain measurements are currently documented in this repository.** Do not treat example calculations as measured robot performance.

---

## 2. Electrical, power, and sensor architecture

This section should explain how electrical energy reaches each subsystem, how control signals are distributed, and how sensors provide information to the controller.

### Current firmware pin references

The existing source code defines the following pin assignments. These are **software constants found in the current code**, not a verified wiring diagram:

| Function | Pin in source | File |
|---|---:|---|
| Motor encoder input | D3 | `Code/motor.cpp` |
| Motor driver enable / PWM | D5 | `Code/motor.cpp` |
| Motor driver direction input 1 | D7 | `Code/motor.cpp` |
| Motor driver direction input 2 | D4 | `Code/motor.cpp` |
| Steering servo signal | D5 | `Code/sterring.cpp` |

**Important integration issue:** the current source assigns D5 to both the motor driver's enable/PWM signal and the steering servo signal. Confirm the actual board and wiring, then resolve this pin conflict before treating the firmware as a working integrated configuration. Update the code and wiring diagram together so that they remain consistent.

### Power distribution

The repository contains `Code/power.cpp` and `Code/power.h`, but both are currently empty. A complete power design has not yet been documented here.

Add a power diagram that identifies:

- Battery chemistry, nominal voltage, capacity, and protection method.
- Main power switch, fuse, and emergency power-disconnection method.
- Voltage regulators or DC/DC converters and their output rails.
- Which rail supplies the controller, motor driver, steering actuator, and sensors.
- Expected and measured current draw for each subsystem.
- Common-ground and signal-reference arrangements.
- Wire gauge, connectors, and any protection against reverse polarity or short circuits.

A power budget should use the real component datasheets and measured current values. State whether each value is a datasheet maximum, a design estimate, or a measurement taken during testing.

### Sensors and calibration

The current source files show an encoder input used for motor-speed feedback. They do not yet document a complete sensor suite or a field-perception system.

For every sensor used on the physical robot, add its model, purpose, interface, mounting position, field of view or measurement range, update rate, and calibration procedure. Explain why its location is appropriate for the robot's geometry and the competition field.

**Sensor inventory, placement diagram, calibration procedure, and wiring diagram — To be completed.**

Store readable electrical schematics in `Elec/` and link them here. Include a high-resolution PNG or PDF preview so evaluators can inspect the connections without installing specialist software.

---

## 3. Software architecture

The firmware is written in Arduino C++ and is divided into source/header pairs. This separation is intended to keep the main program, motor functions, steering functions, and serial communication easier to understand and maintain.

### Firmware modules

| File | Responsibility visible in the current source |
|---|---|
| `Code/main.ino` | Calls motor and UART initialization and runs the current motor test loop |
| `Code/motor.h` / `Code/motor.cpp` | Motor initialization, direction, encoder pulse timing, RPM estimate, PWM output, and speed-control gains |
| `Code/sterring.h` / `Code/sterring.cpp` | Servo initialization and angle command interface; PID steering routine is unfinished |
| `Code/uart.h` / `Code/uart.cpp` | Serial initialization and basic line-based send/receive functions |
| `Code/power.h` / `Code/power.cpp` | Reserved for power-related code; currently empty |

### Motor speed feedback

The motor module attaches an interrupt to the encoder input. Each rising edge records a timestamp using `micros()`, and the time between consecutive pulses is stored as the pulse period. The `currentRpm()` function estimates rotational speed from that period and returns zero when no recent pulse has been received.

The conversion in the current source uses a factor of 10 in the RPM calculation. This implies an assumed encoder pulse count of 10 per revolution in the calculation; confirm the encoder's actual pulses per revolution and any gearbox relationship before relying on the reported RPM.

### Motor control loop

The `motorRun()` function checks the elapsed time and updates the motor command approximately every 50 milliseconds. It compares the requested speed with the measured RPM, calculates an error and a change-in-speed term, updates the PWM command, constrains the output to the 0–255 range, and writes the result to the motor driver's enable pin.

The gains can be changed through `setKp()` and `setKd()`. The current values in the main test loop are test settings, not evidence of a fully tuned controller. Record the tuning method, test conditions, and measured response before describing the controller as validated.

### Main program and current test behaviour

The current `main.ino` performs these actions:

1. Initializes the motor module.
2. Initializes UART serial communication.
3. Sets the motor direction.
4. Repeatedly sends the measured motor speed over serial.
5. Sets the proportional gain to 0.5, requests a speed setpoint of 200, and calls the motor update function.

This is a motor-control test loop. The current main program does not yet demonstrate a complete WRO autonomous navigation strategy, obstacle detection pipeline, lap logic, or parking state machine.

### Serial communication

The UART module starts serial communication at **115200 baud** and provides a line-based send function. The receive function reads incoming text until a newline character is found. A complete communication protocol should document message format, units, valid ranges, update frequency, timeout behaviour, and how invalid or missing commands are handled.

### Software flow and autonomous logic

**To be completed:** add a flowchart for the final program, explain the states and transitions, and document how the robot decides what to do in each competition situation. If lane following, obstacle avoidance, or parking is implemented in later code, link the exact source files and explain the algorithm and its edge cases here.

---

## 4. Obstacle strategy and autonomous behaviour

A strong autonomous strategy must connect observations from the field to safe movement decisions. This section should describe the actual implemented strategy and should be updated as the software develops.

Document the following for the final robot:

- How the robot detects the track boundaries and estimates its position.
- How it identifies obstacles and determines a safe passing side.
- How it chooses between normal lane following and obstacle avoidance.
- How it handles corners, narrow passages, unexpected readings, and blocked paths.
- How it detects and performs the required parking manoeuvre.
- What happens when a sensor reading is missing, inconsistent, or outside its expected range.
- Which safety action has priority when two behaviours request conflicting movements.

Include a state-machine diagram or flowchart and annotated images from real tests. Explain the input, decision, and output for each important state.

**Status:** the current committed firmware does not yet contain enough code to substantiate a completed obstacle-avoidance or autonomous-navigation algorithm. This section is therefore a documentation plan, not a claim that these behaviours are already implemented.

---

## 5. Systems engineering and design decisions

The robot is a system of connected subsystems. A change to one part can affect other parts: motor selection affects the power budget and chassis layout; sensor placement affects detection quality and mounting; controller pin assignments affect wiring and software integration.

For each important design decision, record:

| Decision | Options considered | Reason for final choice | Evidence / trade-off |
|---|---|---|---|
| Drive motor and drivetrain | To be completed | To be completed | Datasheet calculation and driving tests |
| Steering mechanism | To be completed | To be completed | Turning radius and repeatability tests |
| Controller and electronics | To be completed | To be completed | I/O, processing, power and integration needs |
| Sensor selection and placement | To be completed | To be completed | Field coverage and calibration results |
| Battery and power regulation | To be completed | To be completed | Runtime, current draw and safety |

### Constraints and risks

Record the constraints that shaped the build, such as competition dimensions, available materials, component availability, battery limits, fabrication time, processing capacity, and reliability requirements.

Maintain a short risk register. Example categories include loose mechanical fasteners, motor-driver overheating, low battery voltage, electrical shorts, sensor misalignment, encoder noise, and software communication timeouts. For each real risk, document its likelihood, impact, prevention method, and response.

### Design iterations

Do not document only the final version. Keep evidence of meaningful changes:

- What problem was observed?
- What was the suspected cause?
- What change was made?
- What test was repeated?
- What result improved or became worse?
- What decision was made after reviewing the result?

Photographs of prototypes, revised CAD parts, wiring changes, and test setups make the engineering process verifiable.

---

## Testing, calibration, and iteration

Testing should be repeatable. For each test, record the date, robot configuration, battery condition, environment, procedure, number of trials, and result.

Suggested test records:

| Test | What to record | Status |
|---|---|---|
| Motor speed feedback | Requested speed versus measured RPM | To be completed |
| Motor response | Rise time, steady-state error, and stopping behaviour | To be completed |
| Steering | Commanded angle versus measured wheel angle | To be completed |
| UART | Valid messages, malformed messages, and communication loss | To be completed |
| Power | Voltage and current under idle and operating conditions | To be completed |
| Autonomous driving | Successful runs, completion time, and failure cases | To be completed |
| Obstacle handling | Detection success and safe passing results | To be completed |
| Parking | Position accuracy and repeatability | To be completed |

Use measured results rather than statements such as "works perfectly." When a test fails, preserve the result and explain what was changed afterward. This makes the development process useful to evaluators and to anyone reproducing the robot.

---

## Reproducing the project

The goal of this repository is to make the design understandable and, once the missing files are added, reproducible by another team.

### 1. Inspect the hardware documentation

Start with the electrical and mechanical folders. Confirm the component list, controller model, motor-driver model, wiring, battery specifications, and CAD revision before assembling anything.

### 2. Prepare the firmware

The current firmware is located in `Code/`. Open `main.ino` in the Arduino IDE or another compatible Arduino development environment. Install the libraries required by the final source code; the current steering source includes the Arduino Servo library and also includes PID_v1.

Select the exact board and port that match the physical controller. Verify all pin assignments against the wiring diagram before powering the robot. In particular, resolve the D5 motor-enable / servo-signal conflict currently visible in the source.

### 3. Verify the motor subsystem safely

With the robot secured so that its wheels cannot cause an unexpected movement, verify the motor driver wiring, encoder signal, direction, and serial output. Begin with a low command and check that the measured speed behaves plausibly. Confirm the encoder pulses-per-revolution assumption before using RPM values for calibration.

### 4. Integrate and test the complete robot

Connect the subsystems only after checking power polarity, voltage limits, common ground, and wiring continuity. Test one subsystem at a time, then test the integrated system on a controlled area before attempting a full competition run.

### 5. Record the exact working configuration

A reproducible release should identify the controller board, library versions, firmware revision, component models, wiring diagram revision, CAD files, calibration values, and known limitations. Add a release or tagged commit when a configuration has been tested successfully.

**Reproduction status:** the current repository is a starting point, not yet a complete build package. A full bill of materials, verified wiring diagram, CAD exports, sensor documentation, and tested autonomous software still need to be committed.

---

## Current implementation status and next steps

This table distinguishes files that exist from engineering evidence that is still missing.

| Area | Current status | Next action |
|---|---|---|
| Motor firmware | Source files present | Verify encoder scaling and tune speed response |
| Steering firmware | Basic servo interface present | Initialize it in the main program, complete control logic, and resolve pin assignment |
| UART | Basic serial functions present | Define and test a robust message protocol |
| Power software | Empty placeholder files | Add implementation only if required by the final architecture |
| Mechanical design | Folder exists; detailed files not yet documented | Add CAD, dimensions, materials, and assembly views |
| Electrical design | Folder exists; detailed diagrams not yet documented | Add wiring schematic, power budget, and component list |
| Sensors | Encoder input appears in firmware | Document the complete sensor inventory and calibration |
| Autonomous strategy | Not demonstrated by current main program | Add navigation, obstacle, and parking logic with flowcharts |
| Testing | No test results documented here | Add repeatable test procedures and measured results |

### Immediate engineering checklist

- [ ] Confirm the exact controller board and all connected hardware.
- [ ] Resolve the D5 pin conflict between motor PWM and steering servo.
- [ ] Confirm encoder pulses per revolution and RPM calculation.
- [ ] Complete and test the steering initialization and control routine.
- [ ] Add the final wiring and power-distribution diagrams.
- [ ] Add CAD files, dimensions, materials, and assembly instructions.
- [ ] Document every sensor, its placement, and calibration.
- [ ] Add autonomous state-machine and obstacle-strategy documentation.
- [ ] Record test data, failures, fixes, and design iterations.
- [ ] Add clear robot photographs and a reproducible bill of materials.

---

## Acknowledgements and project information

This repository documents the InnoBots team's WRO Future Engineers 2026 engineering project. The contents are maintained as the design and implementation evolve. Hardware specifications, diagrams, performance measurements, and software descriptions should be updated whenever the physical robot or firmware changes.

For questions about the project, use the repository's GitHub Issues or contact the team through its school or competition channels.

---

<p align="center">
  <strong>InnoBots · WRO Future Engineers 2026 · Morocco</strong><br>
  <sub>Design carefully. Test honestly. Document everything.</sub>
</p>
