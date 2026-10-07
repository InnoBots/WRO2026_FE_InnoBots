#include <Arduino.h>
#include <Servo.h>
#include <PID_v1.h>
#include "sterring.h"


#define servoPin 5

Servo sterringServo;

double Kp,Ki,Kd;

void Init(){
 sterringServo.attach(servoPin);
}


void setAngle(int angle){
  sterringServo.write(angle);
}

void updatePID(float _Kp,float _Ki,float _Kd){
  Kp = _Kp;
  Ki = _Ki;
  Kd = _Kd;
}

void PIDsterring(int error){

}


