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
  finally:
    break

while(int(time.strftime('%Y')) < 2016):
  data = com.readline().split(',')
  #print data
  if (data[0]=='$GNRMC'):
    date_str = str(data[9])
    cmd =  '20'+date_str[-2:] + date_str[2:4] + date_str[0:2]
    date_str = str(data[1])
    cmd2 = date_str.split('.')
    cmd3 = cmd2[0]
    cmd3 = cmd3[0:2] + ':' + cmd3[2:4] + ':' + cmd3[4:6]
    os.system('./settime.sh \"%s\"' % (cmd + ' ' + cmd3))
