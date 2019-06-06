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

#setup GPIO to output on pin <output>
GPIO.setup(output, GPIO.OUT)

# Set output PWM to 50 Hz
pwm = GPIO.PWM(output, 50)

# Setup pin for input
GPIO.setup(inp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Initialize output with variable $start
#pwm.start(start)


try:
    # Loop to keep checking input
    # Will update to edge detection
    while True:
        input = GPIO.input(inp)
        if input == True:
            start = 3
            while True:
                pwm.ChangeDutyCycle(start)
                time.sleep(0.5)
                pwm.ChangeDutyCycle(start + 1)
                if start >= 6:
                    start = 3
            print("Input True")
                # time.sleep(0.5)
        else:
            start = 6
            while True:
                pwm.ChangeDutyCycle(start)
                time.sleep(0.5)
                pwm.ChangeDutyCycle(start - 1)
                if start <= 3:
                    start = 6

            # pwm.ChangeDutyCycle(start + 5)
            # time.sleep(0.5)
            # print("Input False")
            # time.sleep(0.5)
except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
