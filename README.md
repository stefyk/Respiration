# Respiration
This code is a work in progress. I have connected my breathing sensor to a relaxation oscillator, whose frequency is changing based on the change in capacitance. The output of the relaxation oscillator is fed into a MCP3208 and connected to a Raspberry PI III. MCP3208 is a 12-bit ADC, which takes an input from the relation oscillator and outputs a digital output to the Raspberry PI III. The code aims to detect the time between rising edge and then to turn this time into frequency. Finally, the frequency shift is going to be measured and displayed, using matplotlib python library.

Code is adapted and reworked from: https://www.raspberrypi.org/forums/viewtopic.php?t=229351
