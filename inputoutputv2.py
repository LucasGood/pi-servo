import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    input = GPIO.input(16)
    if (input == True):
        print("input true")
    else:
        print("input false")
        
