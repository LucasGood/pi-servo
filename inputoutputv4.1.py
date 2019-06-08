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

try:
    # Loop to keep checking input
    # Will update to edge detection
    while True:
        input = GPIO.input(inp)
        if input == True:
            print("Input True")
            start = 3
            pwm.start(start)
            while input == True:
                pwm.ChangeDutyCycle(start)
                print(start)
                time.sleep(0.5)
                pwm.ChangeDutyCycle(start + 1)
                print(start)
                if start >= 6:
                    start = 3
                    print("Input True")

                # time.sleep(0.5)
        else:
            print("Input False")
            start = 6
            pwm.start(start)
            while input == False:
                pwm.ChangeDutyCycle(start)
                print(start)
                time.sleep(0.5)
                pwm.ChangeDutyCycle(start - 1)
                print(start)
                if start <= 3:
                    start = 6
except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
