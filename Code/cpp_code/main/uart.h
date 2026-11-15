#ifndef UART_H
#define UART_H

extern int motorSpeed ,steerError ;
extern double Kp;
extern double Ki;
extern double Kd;

void Init_uart();
void serial_send(String input);
String serial_receive();
void update_serial();
#endif