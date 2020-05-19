#!/usr/bin/env python

# test_freq.py
# 2019-09-24
# Public Domain

import sys
import time
import pigpio

PWM=10

pi = pigpio.pi()

if not pi.connected:
   exit()

args = len(sys.argv)

if args > 1:
   freq = int(sys.argv[1])
else:
   freq = 1000

if args > 2:
   run_for = int(sys.argv[2])
else:
   run_for = 60

cb = pi.callback(PWM) # just count edges on PWM GPIO

start = cb.tally()

pi.hardware_PWM(PWM, freq, 500000) # square wave

time.sleep(run_for)

end = cb.tally()

pi.hardware_PWM(PWM, 0, 0) # stop PWM

cb.cancel() # cancel callback

count = end - start

print("freq={} secs={} count={} actual={:.1f}".format(freq, run_for, count, count/run_for))

pi.stop()