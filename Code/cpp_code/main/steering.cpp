
#include <Arduino.h>
#include <PID_v1.h>
#include "steering.h"
#include <Servo.h>
#include "uart.h"
#define SERVO_PIN 9

Servo steeringServo;

double targetHeading = 0.0;
double currentHeading = 0.0;
double steeringCorrection = 0.0;

double old_Kp = 1, old_Ki = 0, old_Kd = 0;

PID steeringPID(
    &currentHeading,
    &steeringCorrection,
    &targetHeading,
    Kp, Ki, Kd,
    REVERSE
);

const int centerAngle = 90;
const int minAngle = 45;
const int maxAngle = 150;

void Init_steering() {
    steeringServo.attach(SERVO_PIN);
    steeringServo.write(centerAngle);

    steeringPID.SetOutputLimits(
        minAngle - centerAngle,
        maxAngle - centerAngle
    );

    steeringPID.SetSampleTime(10);
    steeringPID.SetMode(AUTOMATIC);
}

void updateSteering() {
    if (Kp != old_Kp or Ki != old_Ki or Kd != old_Kd) {
        old_Kp = Kp;
        old_Ki = Ki;
        old_Kd = Kd;
        steeringPID.SetTunings(Kp, Ki, Kd);
        digitalWrite(LED_BUILTIN, 1);
        delay(2);
        digitalWrite(LED_BUILTIN, 0);
    }
    
    currentHeading = steerError;
    if (currentHeading == 0){
        digitalWrite(LED_BUILTIN, 1);
    }else{
        digitalWrite(LED_BUILTIN, 0);
    }
    steeringPID.Compute();

    int servoAngle = centerAngle + (int)steeringCorrection;

    servoAngle = constrain(servoAngle, minAngle, maxAngle);

    steeringServo.write(servoAngle);
}

