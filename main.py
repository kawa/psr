#!/usr/bin/python
# coding:utf-8
import os
import time
import signal
import RPi.GPIO as GPIO
import MFRC522
import subprocess
from subprocess import Popen

########################################
######## SETUP GPIO PINS ###############
########################################

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
button_pin = 40 # BCM = 21
led_red_pin = 38 # BCM = 20
led_green_pin = 36 # BCM = 16

GPIO.setup(button_pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_red_pin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(led_green_pin,GPIO.OUT,initial=GPIO.LOW)

sw_status = 1

########################################
######## PREPARE RED LED ###############
########################################

os.system("setterm -cursor off")
os.system("clear")

GPIO.output(led_red_pin,GPIO.HIGH)

########################################
######## WAIT FOR TAKEOFF ##############
########################################

while True:
    sw_status = GPIO.input(button_pin)
    if sw_status == 1:
        break
    time.sleep(0.03)

GPIO.output(led_red_pin,GPIO.LOW)
GPIO.output(led_green_pin,GPIO.HIGH)

########################################
######## GAME PLAY! GOOOO ##############
########################################

FNULL = open(os.devnull, 'w')

os.system("omxplayer --refresh ps.mp4")
os.system("clear")

# These are blocking codes
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/kurassyu_01.iso")
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/ace2_01.iso")
#os.system("/opt/retropie/emulators/retroarch/bin/retroarch --fullscreen -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/doko_01.iso")

# This is asynchronous
process = Popen(["/opt/retropie/emulators/retroarch/bin/retroarch", "-L", "/opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so", "/home/pi/RetroPie/roms/psx/kurassyu_01.iso"], stdout=FNULL, stderr=subprocess.STDOUT)

########################################
######## WAIT FOR RFID SCAN ############
########################################

continue_reading = True
reader_count = 0

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    continue_reading = False
    process.send_signal(signal.SIGINT)
    process.wait()
    # GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # # If a card is found
    # if status == MIFAREReader.MI_OK:
    #     print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        # print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

        reader_count += 1

        if reader_count > 7:
            continue_reading = False

########################################
######## RFID SCAN! PLAY GAME 2 ########
########################################

process.send_signal(signal.SIGINT)
process.wait()
os.system("/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/lego.iso")

os.system("setterm -cursor on")
GPIO.cleanup()
