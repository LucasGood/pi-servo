import RPi.GPIO as GPIO
import time

# Set output pin
output = 11

# Set GPIO into Board mode
GPIO.setmode(GPIO.BCM)

#setup GPIO to output on pin <output>
GPIO.setup(output, GPIO.OUT)

# Set output PWM to 50 Hz
output-pwm = GPIO.PWM(output, 50)

# Initialize output with duty cycle of X%
output-pwm.start(2.5)

try:
    while True:
        output-pwm.ChangeDutyCycle(5)
        time.sleep(0.5)
        output-pwm.ChangeDutyCycle(10)
        time.sleep(0.5)
        output-pwm.ChangeDutyCycle(15)
        time.sleep(0.5)
        output-pwm.ChangeDutyCycle(20)
        time.sleep(0.5)
        output-pwm.ChangeDutyCycle(25)
        time.sleep(0.5)
        output-pwm.ChangeDutyCycle(30)

except KeyboardInterrupt:
  output-pwm.stop()
  GPIO.cleanup()
