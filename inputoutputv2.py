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

# Initialize output with duty cycle of X%
pwm.start(0)

try:
    while True:
        pwm.ChangeDutyCycle(1)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(2)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(3)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(4)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(6)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(7)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(8)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(9)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)

except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
