import RPi.GPIO as GPIO
import time

# Set output pin
output = 17
#Set input pin
input = 18
# Set GPIO into BCM mode
GPIO.setmode(GPIO.BCM)
# Setup GPIO to output on pin <output>
GPIO.setup(output, GPIO.OUT)
# Setup GPIO input pin
GPIO.setup(input, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Set output PWM to 50 Hz
out = GPIO.OUT(output, 50)
# Set input
inp = GPIO.IN(input)
# Duty Cycle Start Value
start = 2.5
# Initialize output with duty cycle of X%
out.start(start)

try:
    while inp == True:
        while start < 10:
            out.ChangeDutyCycle(start + 1)
            time.sleep(0.5)
            start = start + 1
            print(start)
        if start >=10:
            start = 2.5

except KeyboardInterrupt:
  out.stop()
  GPIO.cleanup()
