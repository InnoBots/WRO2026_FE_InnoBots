import threading
from lds2d import Lidar
import math



cordonates = []
_lock = threading.Lock()


def lidar_task():
    global cordonates

    with Lidar.open("LDROBOT-STL19P", "/dev/ttyAMA2") as lidar:
        for scan in lidar.scans():
            new_points = [
                (p.dist_mm * math.cos(math.radians(p.angle_deg)), -p.dist_mm * math.sin(math.radians(p.angle_deg)))
                for p in scan.valid_points
            ]
            with _lock:
                cordonates = new_points
def start_lidar():
    thread = threading.Thread(target=lidar_task, daemon=True)
    thread.start()
    return thread


def get_cordonates():
    with _lock:
        return cordonates.copy()

def lidar_obstacle():
    for x, y in cordonates:
        if -55 < x < 55 and 40 < y < 250:
            return True
    return False
def right_obstacle():
    for x, y in cordonates:
        if 0 < x < 55 and 60 < y < 250:
            return True
    return False
def left_obstacle():
    for x, y in cordonates:
        if -55 < x < 0 and 60 < y < 250:
            return True
    return False


def lidar_error():
    points = get_cordonates()

    left_distances = [
        math.hypot(x, y)
        for x, y in points
        if x < 0 and 0 < y 
    ]

    right_distances = [
        math.hypot(x, y)
        for x, y in points
        if x > 0 and 0 < y 
    ]

    if not left_distances or not right_distances:
        return None

    left_distance = sum(left_distances) / len(left_distances)
    right_distance = sum(right_distances) / len(right_distances)

    return right_distance - left_distance




