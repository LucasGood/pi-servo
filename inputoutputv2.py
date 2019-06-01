import RPi.GPIO as GPIO
import time

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
# Initialize output with duty cycle of X%
pwm.start(start)

try:
    while True:
        pwm.ChangeDutyCycle(start + 1)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 2)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 3)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 4)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 6)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 7)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 8)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(start + 9)
        time.sleep(0.5)


except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
