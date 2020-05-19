import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) #using this wiring mode from library
SEN = 21  #channel identifier
GPIO.setup(SEN, GPIO.IN) #setup channel into input mode

#spi_channel = 0
	   
#Enable SPI
#spi = spidev.SpiDev(0, spi_channel)
#spi.open(0,0)
#spi.max_speed_hz = 100000

def callback_up(SEN):
    sleep(0.005)
    if GPIO.input(SEN):  #if port 21 ==1
        print "Rising edge detected!" 
    else:
        print "Falling edge detected!"
  

GPIO.add_event_detect(SEN, GPIO.BOTH, callback=callback_up, bouncetime=5)


try:
    while 1:
        sleep(10)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup([SEN])


