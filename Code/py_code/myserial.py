import serial

PORT = "/dev/ttyAMA0"
BAUDRATE = 115200

ser = serial.Serial(
    port=PORT,
    baudrate=BAUDRATE,
    timeout=0.1,
)

def write_to_serial(data):
    ser.write((data + "\n").encode("utf-8"))