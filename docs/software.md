# Software Architecture

The software architecture is divided between a Raspberry Pi 5 and an STM32 Blue Pill microcontroller, allowing each device to focus on the tasks it performs best.

The Raspberry Pi 5 is responsible for image processing and high-level decision making. Using OpenCV, images captured by the Raspberry Pi Camera Module 3 are analyzed to detect track boundaries, identify obstacles, and determine the appropriate path to follow. Once a navigation decision is made, the Raspberry Pi sends commands to the STM32 through UART serial communication.

The STM32 Blue Pill handles real-time vehicle control. It receives commands from the Raspberry Pi and translates them into steering and speed adjustments. The STM32 directly controls the brushless motor through the ESC and operates the SG90 servo motor used for steering.

To improve navigation accuracy and reduce the risk of collisions, the STM32 continuously reads data from the Sharp GP2Y0A21YK0F infrared distance sensor. A PID controller is implemented to process this sensor data and automatically correct the vehicle's trajectory. This allows the robot to maintain a safe distance from walls, perform smoother turns, and react more effectively when approaching obstacles.

By separating computer vision from low-level control, the system remains responsive even when image-processing tasks become computationally intensive. This architecture provides reliable communication, stable vehicle control, and efficient autonomous navigation during operation.
