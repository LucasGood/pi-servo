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
try:
    pwm.start(3)
    while True:
        # Set PWM to 4 if input TRUE
        GPIO.wait_for_edge(inp, GPIO.RISING)
        pwm.ChangeDutyCycle(4)
        print("Fall on pin {0} ".format(inp))
        GPIO.wait_for_edge(inp, GPIO.FALLING)
        # Set PWM to 6 if innput TRUE
        pwm.ChangeDutyCycle(6)
        print("Rise on pin {0} ".format(inp))
except KeyboardInterrupt:
    GPIO.cleanup
    pwm.stop()
