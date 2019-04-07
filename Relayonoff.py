# !/usr/bin/python


import RPi.GPIO as GPIO
import blynklib
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinList = [2, 3, 4, 17, 27, 22, 10, 9,11]

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

p=GPIO.PWM(11,50)
p.start(7.5)

auth_token = '7d3e86bfe77a401e914c05549ac2ed5f'

# Initialize Blynk

blynk = blynklib.Blynk(auth_token)

# this will initialize relay on & off with blynk app

@blynk.handle_event('write V0')
def write_handler_pin_handler(pin, value):
    Relay1 = (format(value[0]))
    if Relay1 == "0":
        GPIO.output(2, GPIO.LOW)
        print("R1-On")
    else:
        GPIO.output(2, GPIO.HIGH)
        print("R1-Off")


@blynk.handle_event('write V1')
def write_handler_pin_handler(pin, value):
    Relay2 = (format(value[0]))
    if Relay2 == "0":
        GPIO.output(3, GPIO.LOW)
        print("R2-On")
    else:
        GPIO.output(3, GPIO.HIGH)
        print("R2-Off")

@blynk.handle_event('write V2')
def write_handler_pin_handler(pin, value):
    Relay3 = (format(value[0]))
    if Relay3 == "0":
        GPIO.output(4, GPIO.LOW)
        print("R3-On")
    else:
        GPIO.output(4, GPIO.HIGH)
        print("R3-Off")


@blynk.handle_event('write V3')
def write_handler_pin_handler(pin, value):
    Relay4 = (format(value[0]))
    if Relay4 == "0":
        GPIO.output(17, GPIO.LOW)
        print("R4-On")
    else:
        GPIO.output(17, GPIO.HIGH)
        print("R4-Off")

@blynk.handle_event('write V4')
def write_handler_pin_handler(pin, value):
    Relay5 = (format(value[0]))
    if Relay5 == "0":
        GPIO.output(27, GPIO.LOW)
        print("R5-On")
    else:
        GPIO.output(27, GPIO.HIGH)
        print("R5-Off")


@blynk.handle_event('write V5')
def write_handler_pin_handler(pin, value):
    Relay6 = (format(value[0]))
    if Relay6 == "0":
        GPIO.output(22, GPIO.LOW)
        print("R6-On")
    else:
        GPIO.output(22, GPIO.HIGH)
        print("R6-Off")

@blynk.handle_event('write V6')
def write_handler_pin_handler(pin, value):
    Relay7 = (format(value[0]))
    if Relay7 == "0":
        GPIO.output(10, GPIO.LOW)
        print("R7-On")
    else:
        GPIO.output(10, GPIO.HIGH)
        print("R7-Off")

@blynk.handle_event('write V7')
def write_handler_pin_handler(pin, value):
    Relay8 = (format(value[0]))
    if Relay8 == "0":
        GPIO.output(9, GPIO.LOW)
        print("R8-On")
    else:
        GPIO.output(9, GPIO.HIGH)
        print("R8-Off")
# this will initialize servo to rotate

@blynk.handle_event('write V8')
def write_handler_pin_handler(pin, value):
    Doorlock = (format(value[0]))
    if Doorlock =="0":
        p.ChangeDutyCycle(12.5)
        print("Door Locked")
    elif Doorlock =="1":
        p.ChangeDutyCycle(7.5)
        print("Door Unlocked")
try:
    while True:
        blynk.run()

except KeyboardInterrupt:
    print("Quit")

# Reset GPIO settings
GPIO.cleanup()
