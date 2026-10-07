#ifndef MOTOR_H
#define MOTOR_H

void Init_motor();
void motorSetSpeed(int speed);
int motorGetSpeed();
int motorGetPwm();
void motorStop();
void setKp(float Kp);
void setKd(float Kd);
void motorRun();
void direction(bool inverted);
int currentRpm();
void pulse();
#endif