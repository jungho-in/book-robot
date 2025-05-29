import RPi.GPIO as GPIO
import time

LINE_PIN = 17  # BCM 핀 번호

GPIO.setmode(GPIO.BCM)
GPIO.setup(LINE_PIN, GPIO.IN)

try:
    while True:
        val = GPIO.input(LINE_PIN)
        print("Line Sensor Value (Digital):", val)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
