#include <Arduino.h>

#define uart_speed 115200

int motorSpeed = 0,steerError = 0;

double Kp = 2.0;
double Ki = 0.0;
double Kd = 0.0;



void Init_uart(){
    Serial.begin(uart_speed);
    delay(50);
}

void serial_send(String input){
  Serial.println(input);
}

String serial_receive(){
    if (Serial.available() > 0) {
      String inputString = Serial.readStringUntil('\n');
      return inputString;
    }
}

bool update_serial() {
    if (!Serial.available()) return false;

    String line = Serial.readStringUntil('\n');

    int firstComma = line.indexOf(',');
    int secondComma = line.indexOf(',', firstComma + 1);
    int thirdComma = line.indexOf(',', secondComma + 1);
    int fourthComma = line.indexOf(',', thirdComma + 1);

    if (firstComma < 0 || secondComma < 0 ||
        thirdComma < 0 || fourthComma < 0) return false;

    motorSpeed = line.substring(0, firstComma).toInt();
    steerError = line.substring(firstComma + 1, secondComma).toInt();

    Kp = (line.substring(secondComma + 1, thirdComma).toDouble());
    Ki = (line.substring(thirdComma + 1, fourthComma).toDouble());
    Kd = (line.substring(fourthComma + 1).toDouble());

    return true;
}