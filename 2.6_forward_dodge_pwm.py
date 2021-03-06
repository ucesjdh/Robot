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
DutyCycle = 60
#Setting the duty cycle to 0 means motors will not turn
Stop = 0

# set GPIO pin mode
GPIO.setup(AFwd, GPIO.OUT)
GPIO.setup(ABwd, GPIO.OUT)
GPIO.setup(BFwd, GPIO.OUT)
GPIO.setup(BBwd, GPIO.OUT)

print("here")

#set the GPIO to use PWM at a set Hz
pwmAFwd = GPIO.PWM(AFwd,Frequency)
pwmABwd = GPIO.PWM(ABwd,Frequency)
pwmBFwd = GPIO.PWM(BFwd,Frequency)
pwmBBwd = GPIO.PWM(BBwd,Frequency)

#Start the software PWM with a duty cycle of 0 i.e. not moving
pwmAFwd.start(Stop)
pwmABwd.start(Stop)
pwmBFwd.start(Stop)
pwmBBwd.start(Stop)

# turn all motors off
def stopmotors():
    pwmAFwd.ChangeDutyCycle(Stop)
    pwmABwd.ChangeDutyCycle(Stop)
    pwmBFwd.ChangeDutyCycle(Stop)
    pwmBBwd.ChangeDutyCycle(Stop)


# turn both fwd
def forwards():
    pwmAFwd.ChangeDutyCycle(DutyCycle)
    pwmABwd.ChangeDutyCycle(Stop)
    pwmBFwd.ChangeDutyCycle(DutyCycle)
    pwmBBwd.ChangeDutyCycle(Stop)
    
# turn both bwd
def backwards():
    pwmAFwd.ChangeDutyCycle(Stop)
    pwmABwd.ChangeDutyCycle(DutyCycle)
    pwmBFwd.ChangeDutyCycle(Stop)
    pwmBBwd.ChangeDutyCycle(DutyCycle)


# turn both bwd
def left():
    pwmAFwd.ChangeDutyCycle(Stop)
    pwmABwd.ChangeDutyCycle(DutyCycle)
    pwmBFwd.ChangeDutyCycle(DutyCycle)
    pwmBBwd.ChangeDutyCycle(Stop)


# turn both bwd
def right():
    pwmAFwd.ChangeDutyCycle(DutyCycle)
    pwmABwd.ChangeDutyCycle(Stop)
    pwmBFwd.ChangeDutyCycle(Stop)
    pwmBBwd.ChangeDutyCycle(DutyCycle)


# define GPIO pins to use on Pi
pinTrigger = 17
pinEcho = 18

# set pins as input and output
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)


def measure():
    # set trigger to false (low)
    GPIO.output(pinTrigger, False)

    # Allow module to settle
    time.sleep(0.5)

    # send 10us pulse to trigger
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    # start timer
    StartTime = time.time()

    # the start time is reset until the echo pin is high
    while GPIO.input(pinEcho) == 0:
        StartTime = time.time()

    # stop when the echo pin is no longer high
    while GPIO.input(pinEcho) == 1:
        StopTime = time.time()
        # if sensor is too close, it cannot read rebound in time so it flags this
        if StopTime - StartTime >= 0.04:
            print("Too close, to see")
            StopTime = StartTime
            break

    # calculate pulse length
    ElapsedTime = StopTime - StartTime

    # Distance pulse travelled in time is
    distance = ElapsedTime * 34326

    # remove two way travel
    distance = distance / 2

    return distance


def avoider(SafeDistance):
    distance = measure()
    if distance < SafeDistance:
        print(" unsafe measurement:" + str(distance))
        return True
    else:
        print("safe measurement:" + str(distance))
        return False


def dodger(DodgeDistance):
    distance = measure()
    while distance < DodgeDistance:
        left()
        print("dodging left")
        break
        

    # print("dodging measurement: " + str(distance))


try:
    # set trigger to False (low)
    GPIO.output(pinTrigger, False)

    # allow to settle
    time.sleep(0.1)

    # repeat next forever
    while True:
        if avoider(60) is False:
            forwards()
            time.sleep(0.1)
        if avoider(60) is True:
            dodger(60)

except KeyboardInterrupt:
    GPIO.cleanup()

