#include <Arduino.h>
#include "motor.h"


volatile unsigned long lastPulse = 0;
volatile unsigned long period = 0;
#define encoderPin 3
#define EN 5
#define IN1 7
#define IN2 4


double Kp_motor = 1.0, Kd_motor = 0.0;

int rpm, Setpoint = 0, pwm = 0;
float error, dt, previousSpeed = 0, derivative;

unsigned long lastTime = 0;


void Init_motor() {
  pinMode(encoderPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(encoderPin), pulse, RISING);

  pinMode(EN, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(EN, 0);  // speed 0-255

}
void motorSetSpeed(int speed){
    Setpoint = speed;
}
int motorGetSpeed(){
  return currentRpm();
}
int motorGetPwm(){
  return pwm;
}
void motorRun() {
  
  
  unsigned long now = millis();
  
  
  if (now - lastTime >= 50) {
    dt = (now - lastTime) / 1000.0;
    lastTime = now;

    error = Setpoint - currentRpm();
    derivative = -(currentRpm() - previousSpeed) /dt;
    pwm += Kp_motor * error * dt + derivative * Kd_motor;

    pwm = constrain(pwm, 0, 255);
    previousSpeed = currentRpm();
    analogWrite(EN, pwm);
  }
  
  
}
void motorStop(){
  Setpoint = 0 ;
  pwm = 0;
}
void setKp(float Kp){
  Kp_motor = Kp;
}
void setKd(float Kd){
  Kd_motor = Kd;
}
void direction(bool inverted){
  if (inverted){
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
  } else {   
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
  }
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








