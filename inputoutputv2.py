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
pwm.start(2.5)

try:
    while True:
        pwm.ChangeDutyCycle(5)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(15)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(20)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(25)
        time.sleep(0.5)
        pwm.ChangeDutyCycle(30)

except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
