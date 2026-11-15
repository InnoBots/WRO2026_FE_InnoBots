#include <Arduino.h>
#include "power.h"
float voffset = 0.3,aoffset = 0;
const float sensitivity = 0.185;

#define battery_pin A0
#define currentSensor A1

void Init_powerControl(){
  pinMode(battery_pin, INPUT);
  pinMode(currentSensor, INPUT);
}

float battery_voltage(){
  return ((analogRead(battery_pin) * 10.0) / 1023.0 ) + voffset;
}

float pi_current(){
  float voltage = analogRead(currentSensor) * (5.0 / 1023.0);
  float current = (voltage - 2.5+ aoffset) / sensitivity;
  return analogRead(currentSensor);
}