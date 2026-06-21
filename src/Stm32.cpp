#include <Servo.h>


Servo esc;
Servo servo;

const uint8_t ESC_PIN = PB0;
const uint8_t SERVO_PIN = PB1;
String data;
String header;
String value;
int int_value = 0,int_header = 0,s1,s2,error,speed = 30;


float Kp = 0.045;
float Ki = 0.0;
float Kd = 0.02;

float integral = 0;
float prevError = 0;

float servoAngle = 50;

void setup() {
    Serial.begin(115200);
    Serial1.begin(115200);
    pinMode(PA6,INPUT);
    pinMode(PA7,INPUT);

    servo.attach(SERVO_PIN);
    esc.attach(ESC_PIN, 1000, 2000);
    delay(100);
    esc.write(0);
   
    servo.write(servoAngle);
}

void loop() {
  s1 = analogRead(PA6);
  s2 = analogRead(PA7);
  error = (s1-s2);

  if (Serial1.available()) {
        data = Serial1.readStringUntil('\n');

        if (data.length() >= 2) {
             header = data.substring(0, 2);
             value = data.substring(2);
             int_header = header.toInt();
             int_value = value.toInt();
        }
          switch (int_header) {
        case 1:
            servo.write(PID(error));
            esc.write(25);
            break;
        case 2:
            esc.write(20);
            servo.write(PID(int_value));
            break;

        default:
            servo.write(50);
            esc.write(0);
            break;
    }    
          
    }
  
}

float PID(float error){
    integral += error;

    float derivative = error - prevError;

    float output =
        Kp * error +
        Ki * integral +
        Kd * derivative;

    prevError = error;

    servoAngle = constrain(50 + output, 20, 80);

    return servoAngle;
}
