import RPi.GPIO as GPIO
import time

# ----OUTPUT----
#  pin no.
output = 17

# ----INPUT----
#  pin no.
inp = 4

# Set GPIO into BCM mode
GPIO.setmode(GPIO.BCM)

#setup GPIO output
GPIO.setup(output, GPIO.OUT)

# Setup GPIO input
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set output PWM to 50 Hz
pwm = GPIO.PWM(output, 50)

# Setup edge/event detection
#try:
while True:
    GPIO.wait_for_edge(inp, GPIO.RISING)
    print("Rise on pin {0} ".format(inp))

    GPIO.cleanup
pwm.stop()
