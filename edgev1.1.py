import RPi.GPIO as GPIO
import time

# ----INPUT----
#  pin no.
inp = 4

# Set GPIO into BCM mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO input
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

rise = GPIO.wait_for_edge(inp, GPIO.RISING)
fall = GPIO.wait_for_edge(inp, GPIO.FALLING)

# Setup edge/event detection
while True:
    if rise is None:
        print("Nothing")
    else:
        print("Edge detected on {0} ".format(inp))
