import serial

com = serial.Serial('/dev/ttyACM0')
while(True):
	data = com.readline().split(',')
	if (data[0]=='$GNRMC'):
		print data[1], data[9]

