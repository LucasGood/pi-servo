import RPi.GPIO as GPIO
import time

# ----OUTPUT----
# Set output pin
output = 17

# Set GPIO into BCM mode
GPIO.setmode(GPIO.BCM)

#setup GPIO to output on pin <output>
GPIO.setup(output, GPIO.OUT)

# Set output PWM to 50 Hz
pwm = GPIO.PWM(output, 50)

# Duty Cycle Start Value
start = 2.5

# ----INPUT----
# Set input pin
inp = 18

# Setup pin for input
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Assign input to variable

input = GPIO.input(inp)

# Initialize output with duty cycle of X%
pwm.start(start)


while True:
    try:
        while input == True:
            while start < 10:
                pwm.ChangeDutyCycle(start + 1)
                time.sleep(0.5)
                start = start + 1
                print(start)
                if start >=10:
                    start = 2.5

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
