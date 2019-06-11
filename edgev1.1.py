import RPi.GPIO as GPIO
import time

# ----INPUT----
#  pin no.
inp = 4

# Set GPIO into BCM mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO input
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

channel-rise = GPIO.wait_for_edge(inp, GPIO_RISING)
channel-fall = GPIO.wait_for_edge(inp, GPIO_FALLING)

# Setup edge/event detection
try:
    pwm.start(3)
    if channel.rise == True:
        print("rise")
    if channel.fall == True:
        print("fall")

except KeyboardInterrupt:
    GPIO.cleanup
    pwm.stop()
