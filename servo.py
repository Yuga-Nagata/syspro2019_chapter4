import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(arg):
	duty = ( (2.4-0.5)*(arg+90)/180 + 0.5 ) / 20 * 100
	servo.ChangeDutyCycle(duty)

setservo(-90)
time.sleep(1.0)

setservo(0)
time.sleep(1.0)

setservo(90)
time.sleep(1.0)

GPIO.cleanup()
