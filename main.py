#!/usr/bin/python 
# coding:utf-8 
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
 
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
sw_status = 1
 
while True:
    sw_status = GPIO.input(18)
    if sw_status == 0:
        print("OK!")
        break
    time.sleep(0.03)
 
GPIO.cleanup()
