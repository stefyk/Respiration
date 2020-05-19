import spidev
import time
from time import sleep
import RPi.GPIO as GPIO

spi_channel = 0
	   
#Enable SPI
spi = spidev.SpiDev(0, spi_channel)
spi.open(0,0)
spi.max_speed_hz = 50000

# Hardware SPI configuration (wiring explained in README file):
#SPI_PORT   = 0
#SPI_DEVICE = 0

#checks whether the GPIO output is detecting rising edge
#measures the time between two rising edge

lasttime=time.time()
counter=0
 
def callback_up(channel):
    global lasttime
    global counter
    counter = counter + 1
    if counter %100 == 0:
        now = time.time() #system time at the moment
        gap=now-lasttime  #print the difference
        #print(gap)
        frequency=1000.0/gap
        print(frequency)
        lasttime=now
        counter=0
 
GPIO.setmode(GPIO.BOARD) #using this wiring mode from library
SEN = 21  #channel identifier
GPIO.setup(SEN, GPIO.IN) #setup channel into input mode
try:
    GPIO.add_event_detect(SEN, GPIO.RISING, callback=callback_up)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
   print("Interrupted!")
