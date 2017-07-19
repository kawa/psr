#!/usr/bin/python 
# coding:utf-8 
import time
import os
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BCM)
button_pin = 21
GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
 
sw_status = 1

os.system("setterm -cursor off")
os.system("clear")
 
while True:
    sw_status = GPIO.input(button_pin)
    if sw_status == 1:
        break
    time.sleep(0.03)
 
GPIO.cleanup()

os.system("omxplayer --refresh ps.mp4")
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/kurassyu_01.iso")
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/ace2_01.iso")
os.system("/opt/retropie/emulators/retroarch/bin/retroarch --fullscreen -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/doko_01.iso")
os.system("setterm -cursor on")
