#!/usr/bin/env python
import time
import serial
import os

com = serial.Serial('/dev/ttyACM0')

while(int(time.strftime('%Y')) < 2016):
	data = com.readline().split(',')
	if (data[0]=='$GNRMC'):
		print data[1], data[9]
		date_str = str(data[1]) + ' ' + data[9])
		os.system('date +"%H%M%S.00 %d%m%y" -s %s' % date_str)
		

