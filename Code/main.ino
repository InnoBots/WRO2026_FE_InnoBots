#include "motor.h"
#include "sterring.h"
#include "uart.h"

void setup() {
  Init_motor();
  Init_uart();
  direction(0);

}

void loop() {
  /****motorTest*****/
  uart_send(String(motorGetSpeed()));
  setKp(0.5);
  motorSetSpeed(200);
  motorRun();
  /****************/
}
