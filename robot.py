import RPi.GPIO as GPIO
import time
##import serial
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print('Wait untill device gets connected....')
leds = [21,20,16,12]
##port=serial.Serial("/dev/serial0",9600,timeout=0.5)
for i in leds:GPIO.setup(i,GPIO.OUT)
def Stop():
    for i in leds:GPIO.output(i,False)
def Left():
    print "Turning left"
    GPIO.output(leds[0],True)
    GPIO.output(leds[1],False)
    GPIO.output(leds[2],False)
    GPIO.output(leds[3],True)
    time.sleep(.2)
    GPIO.output(leds[3],False)
    GPIO.output(leds[0],False)

def Right():
    print "Turning Right"
    GPIO.output(leds[0],False)
    GPIO.output(leds[1],True)
    GPIO.output(leds[2],True)
    GPIO.output(leds[3],False)
    time.sleep(.2)
    GPIO.output(leds[1],False)
    GPIO.output(leds[2],False)

def Up():
    print "Moving Forward"
    GPIO.output(leds[0],False)
    GPIO.output(leds[1],True)
    GPIO.output(leds[2],False)
    GPIO.output(leds[3],True)


def Down():
    print "Moving Backward"
    GPIO.output(leds[0],True)
    GPIO.output(leds[1],False)
    GPIO.output(leds[2],True)
    GPIO.output(leds[3],False)
    time.sleep(1)
    GPIO.output(leds[2],False)
    GPIO.output(leds[0],False)
##while(True):
##    rcv = port.readline()
##    print(rcv)
##    if(rcv == "forward"):
##            print("forward")
##            Up()
##    elif(rcv == "back"):
##            print("Back")
##            Down()
##    elif(rcv== "left"):
##            print("left")
##            Left()
##    elif(rcv == "right"):
##            print("right")
##            Right()
##    elif(rcv == "stop"):
##            print("stop")
##            Stop()    

