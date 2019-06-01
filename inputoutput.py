import os
from os import system #not needed
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)


duty = 175 / 18 + 2
GPIO.output(3, True)
pwm.ChangeDutyCycle(duty)
sleep(0)
pwm.ChangeDutyCycle(3, False)
pwm.changeDutyCycle(0)
# while True:
#     input = GPIO.input(16)
#     if (input == True):
#          system('/home/pi/Desktop/175Degrees.py')
#         duty = 175 / 18 + 2
#         GPIO.output(3, True)
#         pwm.ChangeDutyCycle(duty)
#         sleep(0)
#         pwm.ChangeDutyCycle(3, False)
#         pwm.changeDutyCycle(0)
#     else:
#         system('/home/pi/Desktop/90Degrees.py')
#         duty = 60 / 18 + 2
#         GPIO.output(3, True)
#         pwm.ChangeDutyCycle(duty)
#         sleep(0)
#         pwm.ChangeDutyCycle(3, False)
#         pwm.changeDutyCycle(0)


pwm.stop()
GPIO.cleanup()
