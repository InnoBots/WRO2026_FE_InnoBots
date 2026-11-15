#!/bin/bash
set -e

# Configuration
PORT="/dev/ttyAMA0"
BAUD="57600"
GPIO="18"
FQBN="arduino:avr:pro:cpu=16MHzatmega328"

if [ -z "$1" ]; then
    echo "Usage: $0 <sketch_folder>"
    exit 1
fi

SKETCH_DIR="$(realpath "$1")"

if [ ! -d "$SKETCH_DIR" ]; then
    echo "Error: sketch directory not found: $SKETCH_DIR"
    exit 1
fi

INO_FILE="$(find "$SKETCH_DIR" -maxdepth 1 -type f -name '*.ino' -print -quit)"
if [ -z "$INO_FILE" ]; then
    echo "Error: no .ino file found in $SKETCH_DIR"
    exit 1
fi

SKETCH_NAME="$(basename "$INO_FILE" .ino)"
BUILD_DIR="$SKETCH_DIR/build"
HEX_FILE="$BUILD_DIR/$SKETCH_NAME.ino.hex"

# Release RESET if anything fails
release_reset() {
    sudo pinctrl set "$GPIO" op dl >/dev/null 2>&1 || true
}
trap release_reset EXIT INT TERM

# Check tools
for tool in arduino-cli avrdude pinctrl; do
    command -v "$tool" >/dev/null || {
        echo "Error: $tool not found"
        exit 1
    }
done

if [ ! -e "$PORT" ]; then
    echo "Error: serial port $PORT not found"
    exit 1
fi

echo "==> Compiling $SKETCH_NAME..."
mkdir -p "$BUILD_DIR"
arduino-cli compile --fqbn "$FQBN" \
    --output-dir "$BUILD_DIR" "$SKETCH_DIR"

if [ ! -f "$HEX_FILE" ]; then
    echo "Error: HEX file not found: $HEX_FILE"
    exit 1
fi

echo "==> Preparing GPIO$GPIO..."
sudo pinctrl set "$GPIO" op dl

echo "==> Resetting Arduino..."
sudo pinctrl set "$GPIO" dh
sleep 0.1
sudo pinctrl set "$GPIO" dl

echo "==> Uploading through $PORT at $BAUD baud..."
avrdude -p atmega328p -c arduino \
    -P "$PORT" -b "$BAUD" -D \
    -U "flash:w:$HEX_FILE:i"

echo "==> Upload successful!"
