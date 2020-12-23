#distance

import RPi.GPIO as GPIO
import time

#set modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#define GPIO pins to use on Pi
pinTrigger = 17
pinEcho = 18

print("ultrasonic distance")

#set pins as input and output
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

try:
    #repeat indented block forever
    while True:
        #set trigger to false (low)
        GPIO.output(pinTrigger, False)
        
        #Allow module to settle
        time.sleep(0.5)
        
        #send 10us pulse to trigger
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)
        
        #start timer
        StartTime = time.time()
        
        #the start time is reset until the echo pin is high
        while GPIO.input(pinEcho)==0:
            StartTime = time.time()
            
        #stop when the echo pin is no longer high
        while GPIO.input(pinEcho)==1:
            StopTime = time.time()
            #if sensor is too close, it cannot read rebound in time so it flags this
            if StopTime-StartTime >= 0.04:
                print("Too close, to see")
                StopTime = StartTime
                break
            
        #calculate pulse length
        ElapsedTime = StopTime - StartTime
        
        #Distance pulse travelled in time is
        Distance = ElapsedTime * 34326
        
        #remove two way travel
        Distance = Distance/2
        
        print("Distance: %.1f cm" % Distance)
        
        time.sleep(0.5)
        
#if you press ctrl+c interrupt
except KeyboardInterrupt:
    #Reset GPIO settings
    GPIO.cleanup()
