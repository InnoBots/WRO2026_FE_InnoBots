from picamera2 import Picamera2
import cv2
import numpy as np
from gpiozero import Button
from signal import pause
import serial
import time

ser = serial.Serial(
port='/dev/serial0',
baudrate=115200,
timeout=1
)

time.sleep(0.1)

button = Button(17, pull_up=True)

picam2 = Picamera2()

config = picam2.create_video_configuration(
main={"size": (640, 360), "format": "RGB888"}
)

picam2.configure(config)
picam2.start()

================== COLOR SETTINGS ==================

GREEN_H_MIN, GREEN_H_MAX = 40, 85
GREEN_S_MIN, GREEN_V_MIN = 80, 80

RED_S_MIN, RED_V_MIN = 120, 70
RED1 = (0, 10)
RED2 = (170, 180)

kernel = np.ones((5, 5), np.uint8)

================== LARGEST CONTOUR ==================

def largest_contour_center(mask):
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 0:  
    return None, 0  

largest = max(contours, key=cv2.contourArea)  
area = cv2.contourArea(largest)  

if area < 300:  
    return None, 0  

M = cv2.moments(largest)  
if M["m00"] == 0:  
    return None, 0  

cx = int(M["m10"] / M["m00"])  
cy = int(M["m01"] / M["m00"])  

return (cx, cy), area

def relative_pos(cx, center_screen):
return (cx - center_screen) / center_screen

================== MAIN LOOP ==================

while True:
if button.is_pressed:
frame = picam2.capture_array()
frame = cv2.flip(frame, 0)

h, w, _ = frame.shape  
    center_screen = w // 2  

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  

    # ================== GREEN MASK (SMOOTHED) ==================  

    lower_green = np.array([GREEN_H_MIN, GREEN_S_MIN, GREEN_V_MIN])  
    upper_green = np.array([GREEN_H_MAX, 255, 255])  

    mask_green = cv2.inRange(hsv, lower_green, upper_green)  

    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)  
    mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_CLOSE, kernel)  

    mask_green = cv2.GaussianBlur(mask_green, (7, 7), 0)  
    _, mask_green = cv2.threshold(mask_green, 50, 255, cv2.THRESH_BINARY)  

    # ================== RED MASK (SMOOTHED) ==================  

    mask_red = (  
        cv2.inRange(hsv, (RED1[0], RED_S_MIN, RED_V_MIN), (RED1[1], 255, 255)) +  
        cv2.inRange(hsv, (RED2[0], RED_S_MIN, RED_V_MIN), (RED2[1], 255, 255))  
    )  

    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)  
    mask_red = cv2.morphologyEx(mask_red, cv2.MORPH_CLOSE, kernel)  

    mask_red = cv2.GaussianBlur(mask_red, (7, 7), 0)  
    _, mask_red = cv2.threshold(mask_red, 50, 255, cv2.THRESH_BINARY)  

    # ================== DETECT BIGGEST OBJECT ==================  

    green_center, green_area = largest_contour_center(mask_green)  
    red_center, red_area = largest_contour_center(mask_red)  

    # ================== SELECT ONLY BIGGEST COLOR ==================  

    chosen_center = None  
    chosen_color = None  
    chosen_area = 0  

    if green_area >= red_area:  
        chosen_center = green_center  
        chosen_color = "GREEN"  
        chosen_area = green_area  
    else:  
        chosen_center = red_center  
        chosen_color = "RED"  
        chosen_area = red_area  

    # ================== DRAW ONLY ONE RESULT ==================  

    if chosen_center:  
        cx, cy = chosen_center  
        rel = relative_pos(cx, center_screen)  

        color = (0, 255, 0) if chosen_color == "GREEN" else (0, 0, 255)  

        cv2.circle(frame, (cx, cy), 10, color, -1)  
        cv2.putText(frame, f"{chosen_color}: {rel:.2f}",  
                    (10, 40),  
                    cv2.FONT_HERSHEY_SIMPLEX,  
                    0.8,  
                    color, 2)  
        error = int((cx - 320) * 4095 / 320)  
        if chosen_color == "RED":  
            error = error + 3900;  
            print(chosen_color, "pos:", error)  
        elif chosen_color == "GREEN":  
            error = error - 3900;  
            print(chosen_color, "pos:", error)  
        ser.write(f"02{error}\n".encode())  
        ser.flush()  
    else :  
        ser.write("01\n".encode())  
        ser.flush()  
    # ================== DISPLAY ==================  

    cv2.imshow("Frame", frame)  
    cv2.imshow("Green mask", mask_green)  
    cv2.imshow("Red mask", mask_red)  

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

ser.write("0000\n".encode())
ser.flush()
ser.close()

picam2.stop()
cv2.destroyAllWindows()
