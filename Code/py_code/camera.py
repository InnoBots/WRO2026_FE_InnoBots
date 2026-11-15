import threading
import json
import numpy as np
import cv2
from picamera2 import Picamera2

resolution = (1280, 720)
min_area = 5000

COLORS = ["Red", "Green", "Blue", "Orange", "Magenta"]
CONFIG_FILE = "colors_hsv_config.json"

TRACKBAR_NAMES = [
    "H Min", "H Max",
    "S Min", "S Max",
    "V Min", "V Max"
]

_camera = None
_thread = None
_stop_event = threading.Event()

color_configs = {}
color_masks = {
    color.lower(): None for color in COLORS
}


def start_camera():
    """Initialize the camera and start its processing thread."""

    global _camera, _thread, color_configs

    if _thread is not None and _thread.is_alive():
        return _thread

    _stop_event.clear()

    # Load all color configurations
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)

    color_configs = {}

    for color in COLORS:
        values = data[color]

        color_configs[color.lower()] = {
            name: int(value)
            for name, value in zip(TRACKBAR_NAMES, values)
        }

    # Initialize camera
    _camera = Picamera2()

    _camera.configure(
        _camera.create_preview_configuration(
            main={"format": "RGB888", "size": resolution}
        )
    )

    _camera.start()

    _camera.set_controls({
        "AfMode": 0,
        "LensPosition": 5.0,
        "AwbEnable": True
    })

    _thread = threading.Thread(
        target=_camera_loop,
        daemon=True
    )

    _thread.start()

    return _thread


def _camera_loop():
    global color_masks

    # 5×5 kernel used for morphological opening
    kernel = np.ones((5, 5), np.uint8)

    try:
        while not _stop_event.is_set():

            frame = _camera.capture_array()

            frame = cv2.rotate(
                frame, cv2.ROTATE_180
            )

            hsv = cv2.cvtColor(
                frame, cv2.COLOR_RGB2HSV
            )

            masks = {}

            for color in COLORS:

                name = color.lower()
                config = color_configs[name]

                lower = np.array([
                    config["H Min"],
                    config["S Min"],
                    config["V Min"]
                ])

                upper = np.array([
                    config["H Max"],
                    config["S Max"],
                    config["V Max"]
                ])

                mask = cv2.inRange(hsv, lower, upper)

                # Remove small noise with a 5×5 morphological opening
                masks[name] = cv2.morphologyEx(
                    mask,
                    cv2.MORPH_OPEN,
                    kernel
                )

            color_masks = masks

            # Display all frames
            cv2.imshow("Camera", frame)

            for color in COLORS:
                name = color.lower()
                cv2.imshow(color, masks[name])

            if cv2.waitKey(1) & 0xFF == ord("q"):
                _stop_event.set()
                break

    finally:
        cv2.destroyAllWindows()


def stop_camera():
    """Stop the camera thread and release the camera."""

    global _camera, _thread

    _stop_event.set()

    if _thread is not None and _thread.is_alive():
        _thread.join()

    if _camera is not None:
        _camera.stop()
        _camera.close()
        _camera = None

    _thread = None

    for color in COLORS:
        color_masks[color.lower()] = None

    cv2.destroyAllWindows()


def camera_obstacle():
    candidates = []

    for color in ("red", "green"):

        mask = color_masks[color]

        if mask is None:
            continue

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:

            area = cv2.contourArea(contour)

            if area >= min_area:
                candidates.append(
                    (area, color, contour)
                )

    if not candidates:
        return None

    area, color, biggest = max(
        candidates,
        key=lambda item: item[0]
    )

    moments = cv2.moments(biggest)

    if moments["m00"] == 0:
        return None

    center_x = int(
        moments["m10"] / moments["m00"]
    )

    error = center_x - (resolution[0] // 2)

    return error, color