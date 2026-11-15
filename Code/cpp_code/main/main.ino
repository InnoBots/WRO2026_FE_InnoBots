#include "motor.h"
#include "steering.h"
#include "uart.h"



void setup() {
  Init_uart();
  Init_motor();
  Init_steering(); //45--150
  runSpeed(0);
  
 

}

void loop() {
  update_serial();
  updateSteering();
  runSpeed(motorSpeed);


  
}
