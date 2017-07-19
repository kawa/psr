#!/usr/bin/python 
# coding:utf-8 
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
button_pin = 21
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
sw_status = 1
 
while True:
    sw_status = GPIO.input(button_pin)
#    if sw_status == 0:
#        print("OK!")
#        break
    print(sw_status)
    time.sleep(0.03)
 
GPIO.cleanup()
