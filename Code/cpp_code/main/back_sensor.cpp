#include <Arduino.h>
#include "back_sensor.h"


#define left_sensor A2
#define right_sensor A3

void Init_Sensors(){
  pinMode(left_sensor, INPUT);
  pinMode(right_sensor, INPUT);
}
int rightSensor(){
  return analogRead(right_sensor);
}
int leftSensor(){
  return analogRead(left_sensor);
}
int backError(){
  return (rightSensor() - leftSensor());
}