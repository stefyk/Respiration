#This code has been developed, using 
#https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-3-spi-and-analog-input
#This code has been developed, using 
#https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/experiment-3-spi-and-analog-input

import spidev
import time

spi_channel = 0
	   
#Enable SPI
spi = spidev.SpiDev(0, spi_channel)
spi.max_speed_hz = 50000

# Hardware SPI configuration (wiring explained in README file):
#SPI_PORT   = 0
#SPI_DEVICE = 0

def read_adc(adc_channel, Vref = 3.3):
	adc_channel = 0
 	adc = spi.xfer2([6+((4&adc_channel)>>2),(3&adc_channel)<<6,0])
	data = ((adc[1]&15) << 8) + adc[2]
	return data

def ConvertVolts(data):
  volts = (data * 3.3) / float(4096)
  volts = round(volts)
  return volts

while True:
 
  # Read the voltage data
  output_volts = ConvertVolts(data)
 
  # Print out results
  print("The voltage of the channel is: {} ({}V)".format(output_volts))
 
  # Wait before repeating loop
  time.sleep(5)

