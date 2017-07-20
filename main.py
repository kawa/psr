#!/usr/bin/python 
# coding:utf-8 
import time
import os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
button_pin = 21
led_red_pin = 20
led_green_pin = 16

GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_red_pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(led_green_pin,GPIO.OUT,initial=GPIO.LOW)
 
sw_status = 1

os.system("setterm -cursor off")
print("hoge")
os.system("clear")

#time.sleep(6);
GPIO.output(led_red_pin,GPIO.HIGH)

while True:
    sw_status = GPIO.input(button_pin)
    if sw_status == 1:
        break
    time.sleep(0.03)
 
GPIO.output(led_red_pin,GPIO.LOW)
GPIO.output(led_green_pin,GPIO.HIGH)

os.system("omxplayer --refresh ps.mp4")
os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/kurassyu_01.iso")
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/ace2_01.iso")
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch --fullscreen -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/doko_01.iso")
os.system("setterm -cursor on")

GPIO.cleanup()
