#ifndef STERRING_H
#define STERRING_H

void Init();
void setAngle(int angle);

void PIDsterring(int error);
void updatePID(float Kp,float Ki,float Kd);


#endif