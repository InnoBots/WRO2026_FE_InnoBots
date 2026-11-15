import lidar
import controle
import camera
import threading
import time
import myserial as ser
from myserial import write_to_serial as write












def main():
    lidar.start_lidar()
    camera.start_camera()
    print("gg")
    try:
        motorSpeed = 0
        steerError = 0
        
        
        while True:
            # =================== main code =======================
            motorSpeed = 70
            Kp = 0.8  #0.1
            Ki = 0.0 #0.05
            Kd = 0.1 #0.05
            
            cam_ob = camera.camera_obstacle()
            if cam_ob:
                error, color = cam_ob
                while lidar.lidar_obstacle():
                    if color == "red":
                        steerError = 1000
                    elif color == "green":
                        steerError = -1000
                    
                    print("max")
                    packet = f"{motorSpeed},{steerError},{Kp},{Ki},{Kd}"
                    ser.write_to_serial(packet)
                else:
                    steerError = error
                    print(error)
            elif lidar.lidar_obstacle():
                motorSpeed = 0 #-55
                steerError = 0 #-lidar.lidar_error()
                
            else:
                steerError = lidar.lidar_error()
                print("normal")
            # ====================== end ===========================
            packet = f"{motorSpeed},{steerError},{Kp},{Ki},{Kd}"
            ser.write_to_serial(packet)
    except KeyboardInterrupt:
        pass
    finally:
        packet = f"{0},{steerError},{Kp},{Ki},{Kd}"
        ser.write_to_serial(packet)
        camera.stop_camera()

if __name__ == "__main__":
    main()