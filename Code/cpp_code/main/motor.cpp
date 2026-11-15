#include <Arduino.h>
#include "motor.h"
#define encoderPin 3
#define motorPin1 5
#define motorPin2 6



volatile unsigned long lastPulse = 0;
volatile unsigned long period = 0;
int rpm = 0;

void Init_motor() {
  pinMode(encoderPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(encoderPin), pulse, RISING);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  
}

int currentRpm() {
  if (period > 0 && micros() - lastPulse < 500000) {
    rpm = 60000000.0 / (period * 10.0);
  } else {
    rpm = 0;
  }
  return rpm;
}
void pulse() {
  unsigned long now = micros();
  period = now - lastPulse;
  lastPulse = now;
}

void runSpeed(int speed) {
 
  if (speed > 0) {
    analogWrite(motorPin1, speed);
    analogWrite(motorPin2, 0);
  } else if (speed < 0) {
    analogWrite(motorPin1, 0);
    analogWrite(motorPin2, -speed);
  } else {
    analogWrite(motorPin1, 0);
    analogWrite(motorPin2, 0);
  }
}


