#This code has been developed, using 
#https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-3-spi-and-analog-input

import spidev
import time

spi_channel = 0
	   
#Enable SPI
spi = spidev.SpiDev(0, spi_channel)
spi.max_speed_hz = 100000

# Hardware SPI configuration (wiring explained in README file):
SPI_PORT   = 0
SPI_DEVICE = 0


def read_adc(channel, Vref = 3.3):
	 # Make sure ADC channel is 0 or 1
    if channel != 0:
       channel = 1
        
 #adc = spi.xfer2([6+((4&channel)>>2),(3&channel)<<6,0])
 #data = ((adc[1]&15) << 8) + adc[2]
 adc = spi.xfer2([1,(8+channel)<<4,0])
 data = ((adc[1]&3) << 8) + adc[2]
 return data
 
 def Volts(data):
  volts = (data * 3.3) / float(4095)
  volts = round(volts, 2) # Round off to 2 decimal places
  return volts
  
		
while True:
		# The read_adc function will get the value of the specified channel (0-1).
	adc_0 = read_adc(0)
		# Print the ADC values.
	print("The amplitude of V from Ch.0 is:", round(volts, 2),"V")
	time.sleep(0.000025)
