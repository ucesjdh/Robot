import RPi.GPIO as GPIO
import time

#set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define variables for GPIO pins
AFwd = 10
ABwd = 9
BFwd = 8
BBwd = 7

#set GPIO pin mode
GPIO.setup(AFwd, GPIO.OUT)
GPIO.setup(ABwd, GPIO.OUT)
GPIO.setup(BFwd, GPIO.OUT)
GPIO.setup(BBwd, GPIO.OUT)

#turn all motors off
def stopmotors():
    GPIO.output(AFwd, 0)
    GPIO.output(ABwd, 0)
    GPIO.output(BFwd, 0)
    GPIO.output(BBwd, 0)
 
#turn both fwd
def forwards():
    GPIO.output(AFwd, 1)
    GPIO.output(ABwd, 0)
    GPIO.output(BFwd, 1)
    GPIO.output(BBwd, 0)
    
#turn both bwd
def backwards():
    GPIO.output(AFwd, 0)
    GPIO.output(ABwd, 1)
    GPIO.output(BFwd, 0)
    GPIO.output(BBwd, 1)
    
#turn both bwd
def left():
    GPIO.output(AFwd, 0)
    GPIO.output(ABwd, 1)
    GPIO.output(BFwd, 1)
    GPIO.output(BBwd, 0)
    
#turn both bwd
def right():
    GPIO.output(AFwd, 1)
    GPIO.output(ABwd, 0)
    GPIO.output(BFwd, 0)
    GPIO.output(BBwd, 1)
    
right()
time.sleep(1)
left()
time.sleep(1)
forwards()
time.sleep(1)
left()
time.sleep(1)
right()
time.sleep(1)
forwards()
time.sleep(1)

stopmotors()

GPIO.cleanup()
    