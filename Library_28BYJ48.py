import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Définition d'une séquence par demi-step (donc 8 mouvements)
Seq = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]


def pin(in1,in2,in3,in4):
    global StepPins
    StepPins = [in1,in2,in3,in4]
    GPIO.setup(in1,GPIO.OUT)
    GPIO.output(in1, False)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.output(in2, False)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.output(in3, False)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.output(in4, False)


def avancer(angle, vitesse):
    WaitTime = vitesse/4096
    NbStep = int(((4096)/360)*angle)
    StepCounter = 0

    for i in range(NbStep):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += 1

        if (StepCounter==8):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = 7
        time.sleep(WaitTime)
    for pin in StepPins:
        GPIO.output(pin, False)


def reculer(angle, vitesse):
    WaitTime = vitesse/4096
    NbStep = int(((4096)/360)*angle)
    StepCounter = 0

    for i in range(NbStep):
        for pin in range(4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)
        StepCounter += -1

        if (StepCounter==8):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = 7
        time.sleep(WaitTime)
    for pin in StepPins:
        GPIO.output(pin, False)