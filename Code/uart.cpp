#include <Arduino.h>

#define uart_speed 115200

void Init_uart(){
    Serial.begin(uart_speed);
    delay(50);
}

void uart_send(String input){
  Serial.println(input);
}

String uart_recieve(){
    if (Serial.available() > 0) {
      String inputString = Serial.readStringUntil('\n');
      return inputString;
    }
}