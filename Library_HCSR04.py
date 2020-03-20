import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def pin(trig, echo):
    global Trig
    Trig = trig
    global Echo
    Echo = echo
    GPIO.setup(Trig,GPIO.OUT)
    GPIO.setup(Echo,GPIO.IN)
    GPIO.output(Trig, False)

def mesurer():
    
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)
    
    while GPIO.input(Echo)==0:
        debutImpulsion = time.time()

    while GPIO.input(Echo)==1:
        finImpulsion = time.time()

    return(round(((finImpulsion - debutImpulsion) * 17165) -1, 1))
    
    