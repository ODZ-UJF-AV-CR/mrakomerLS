#!/usr/bin/env python
import time
import serial
import os

while (True):
  try:
    com = serial.Serial('/dev/ttyACM0')
  except:
    print 'GPS is not ready'
    time.sleep(5)
    continue
  else:
    break

while(int(time.strftime('%Y')) < 2016):
    try:
	data = com.readline().split(',')
    except:
	print '1 GPS is not ready'
	time.sleep(5)
	continue
    else:
	if (data[0]=='$GNRMC'):
	    date_str = str(data[9])
	    cmd =  '20'+date_str[-2:] + date_str[2:4] + date_str[0:2]
	    date_str = str(data[1])
	    cmd2 = date_str.split('.')
	    cmd3 = cmd2[0]
	    cmd3 = cmd3[0:2] + ':' + cmd3[2:4] + ':' + cmd3[4:6]
	    print cmd, cmd3
	    os.system('/home/odroid/git/mrakomerLS/bat/settime.sh \"%s\"' % (cmd + ' ' + cmd3))
	    com.close()

while(True):
    time.sleep(60**60*24)

    try:
	com = serial.Serial('/dev/ttyACM0')
    except:
	print '1 GPS is not ready'
	continue
    else:
	while(True):
	    try:
		data = com.readline().split(',')
		if (data[0]=='$GNRMC'):
		    date_str = str(data[9])
		    cmd =  '20'+date_str[-2:] + date_str[2:4] + date_str[0:2]
		    date_str = str(data[1])
		    cmd2 = date_str.split('.')
		    cmd3 = cmd2[0]
		    cmd3 = cmd3[0:2] + ':' + cmd3[2:4] + ':' + cmd3[4:6]
		    print cmd, cmd3
		    os.system('/home/odroid/git/mrakomerLS/bat/settime.sh \"%s\"' % (cmd + ' ' + cmd3))
		    com.close()
		    break
	    except:
		print '3 GPS is not ready'
		tiime.sleep(5)
		continue


