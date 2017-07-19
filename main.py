import wiringpi
import time
button_pin = 21

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( button_pin, 0 )
wiringpi.pullUpDnControl( button_pin, 2 )

while True:
    if( wiringpi.digitalRead(button_pin) == 0 ):
        print ("ON")
    else:
        print ("OFF")
