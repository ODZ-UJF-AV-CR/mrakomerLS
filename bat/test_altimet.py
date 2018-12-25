#!/usr/bin/python
#
# Mrakomer poller
# 

#import m_settings as g
import time
import datetime
import logging
import serial
import math
#import threading
from pymlab import config


def handle_data(data):
	print data,
	datafname = '/home/odroid/mrakomer/station/data/' + str(time.strftime("%Y%m%d%H0000000")) + "_LS-M0_meta" + ".csv"
	if int(time.strftime('%Y')) >= 2016:
	#if True:
		with open(datafname, "a") as nbf:
			nbf.write(data)
		nbf.close()



port = '/dev/ttyUSB0'

baud = 2400

while True:
#	try:

		cfg = 	config.Config(
					i2c = {
						"port": 1,
					},
					bus = [
						{
						    "name":          "altimet",
						    "type":        "altimet01",
						},
					],
				)

		cfg.initialize()
		alt = cfg.get_device("altimet")
		time.sleep(0.5)



		while True:
			(t1, p1) = alt.get_tp()
			print t1, p1
			time.sleep(1)

#	except:
#		print "Exception"
#		time.sleep(5)
#		continue

