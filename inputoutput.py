import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    input = GPIO.input(4)
    if (input == True):
        print("input true")
    else:
        print("input false")
