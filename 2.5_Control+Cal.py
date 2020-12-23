# combined mission and stop if distance to object < 20cm

import RPi.GPIO as GPIO
import time

# set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define variables for GPIO pins
AFwd = 10
ABwd = 9
BFwd = 8
BBwd = 7

#Define how many times to turn the pin on and off per second
Frequency = 20
#Define how long the pin stays on each cycle
DutyCycle = 30
#Setting the duty cycle to 0 means motors will not turn
Stop = 0

# set GPIO pin mode
GPIO.setup(AFwd, GPIO.OUT)
GPIO.setup(ABwd, GPIO.OUT)
GPIO.setup(BFwd, GPIO.OUT)
GPIO.setup(BBwd, GPIO.OUT)

#set the GPIO to use PWM at a set Hz

pwmAFwd = GPIO.PWM(AFwd,Frequency)
pwmABwd = GPIO.PWM(ABwd,Frequency)
pwmBFwd = GPIO.PWM(BFwd,Frequency)
pwmBBwd = GPIO.PWM(BBwd,Frequency)


# turn all motors off
def stopmotors():
    GPIO.output(AFwd, 0)
    GPIO.output(ABwd, 0)
    GPIO.output(BFwd, 0)
    GPIO.output(BBwd, 0)


# turn both fwd
def forwards():
    GPIO.output(AFwd, 1)
    GPIO.output(ABwd, 0)
    GPIO.output(BFwd, 1)
    GPIO.output(BBwd, 0)


# turn both bwd
def backwards():
    GPIO.output(AFwd, 0)
    GPIO.output(ABwd, 1)
    GPIO.output(BFwd, 0)
    GPIO.output(BBwd, 1)


# turn both bwd
def left():
    GPIO.output(AFwd, 0)
    GPIO.output(ABwd, 1)
    GPIO.output(BFwd, 1)
    GPIO.output(BBwd, 0)


# turn both bwd
def right():
    GPIO.output(AFwd, 1)
    GPIO.output(ABwd, 0)
    GPIO.output(BFwd, 0)
    GPIO.output(BBwd, 1)