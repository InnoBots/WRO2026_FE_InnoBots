# Hardware Components

The InnoBots vehicle is built using a combination of computing, sensing, power management, and motion control components. Each component was selected based on the requirements of the WRO Future Engineers challenge.

## Raspberry Pi 5

The Raspberry Pi 5 serves as the main computer of the vehicle. It is responsible for processing images from the camera, running computer vision algorithms, making navigation decisions, and communicating with the STM32 microcontroller. OpenCV is used on the Raspberry Pi to analyze the track and detect obstacles.

## STM32 Microcontroller

The STM32 acts as the low-level controller of the system. It receives commands from the Raspberry Pi and controls the hardware in real time. Its tasks include steering control, motor control, sensor reading, and communication with the main computer.

## Raspberry Pi Camera Module 3

The Camera Module 3 is mounted at the front of the vehicle and provides live visual data to the Raspberry Pi. The camera is used for wall detection, obstacle detection, track analysis, and navigation.

## 18650 Lithium Battery Pack

The robot is powered by three 18650 lithium-ion batteries connected in series. This configuration provides the voltage and capacity required to operate all electronic components during testing and competition runs.

## 3S Battery Management System (BMS)

The Battery Management System protects the battery pack from overcharging, over-discharging, and short circuits. It also helps maintain balanced charging between the battery cells, improving safety and battery lifespan.

## XL4016 DC-DC Buck Converter

The XL4016 is used to reduce and regulate the battery voltage before supplying power to the Raspberry Pi and STM32. Stable voltage is important to prevent unexpected resets and ensure reliable operation.

## XL4016 Heatsink

A heatsink is attached to the XL4016 converter to improve heat dissipation. During long periods of operation, the converter can become warm, so additional cooling helps maintain stable performance.

## Raspberry Pi Active Cooler

An active cooling system is installed on the Raspberry Pi 5. Since image processing can place a significant load on the processor, active cooling helps prevent thermal throttling and keeps performance consistent.

## Brushless DC Motor (BLDC)

The vehicle uses a brushless DC motor as its main propulsion system. The motor provides the power required to move the vehicle around the track while maintaining efficient operation and smooth speed control.

## Electronic Speed Controller (ESC)

The ESC controls the speed of the brushless motor. It receives control signals from the STM32 and adjusts the motor speed accordingly. This allows the vehicle to accelerate, slow down, and maintain stable movement.

## SG90 Servo Motor

The SG90 servo motor controls the steering mechanism of the vehicle. By adjusting the steering angle, the robot can navigate corners, avoid obstacles, and follow the desired path.

## Sharp GP2Y0A21YK0F Infrared Distance Sensor

The infrared distance sensor measures the distance between the vehicle and nearby objects. This information is used to assist with obstacle detection and improve navigation accuracy.

## MicroSD Card

The MicroSD card stores the Raspberry Pi operating system, source code, configuration files, and project data. A Class 10 card was selected to ensure fast and reliable access to stored information.

## Wiring Components

Male-to-female Dupont cables, female-to-female Dupont cables, jumper wires, and connectors are used to establish electrical connections between the various components. Heat-shrink tubing and cable ties are used to secure and protect the wiring while improving organization inside the vehicle.

## Mechanical Components

Several custom mechanical parts were designed using SolidWorks and manufactured through 3D printing. These parts include sensor mounts, electronic supports, structural brackets, and component holders. Custom-designed parts allowed us to optimize space usage, improve component placement, and simplify maintenance.
