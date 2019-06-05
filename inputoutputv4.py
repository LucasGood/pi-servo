import RPi.GPIO as GPIO
import time

# ----OUTPUT----
# Set output pin
output = 17

# ----INPUT----
# Set input pin
inp = 4

# Set GPIO into BCM mode
GPIO.setmode(GPIO.BCM)

#setup GPIO to output on pin <output>
GPIO.setup(output, GPIO.OUT)

# Set output PWM to 50 Hz
pwm = GPIO.PWM(output, 50)

# Duty Cycle Start Value
start = 2.5


# Setup pin for input
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Assign input to variable


# Initialize output with variable $start
pwm.start(start)


try:
    # Loop to keep checking input
    # Will update to edge detection
    while True:
        input = GPIO.input(inp)
        while input == True:
            pwm.ChangeDutyCycle(3)
            time.sleep(0.5)
            print("Input True")
            # time.sleep(0.5)
        while input == False:
            pwm.ChangeDutyCycle(start + 5)
            time.sleep(0.5)
            print("Input False")
            # time.sleep(0.5)
except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
