#!/usr/bin/env python

import serial
import time
import signal
import sys
import array
import logging

baud = 57600

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        print("bye")
        arduino.close()
        sys.exit(0)

#print("Installing CTRL-C handler...")
signal.signal(signal.SIGINT, signal_handler)

#print("Opening log file...")
logging.basicConfig(filename="log.txt",level=logging.DEBUG)

#print("Connecting to serial...")
#arduino = serial.Serial('/dev/ttyACM0',baud,timeout=1)
arduino = serial.Serial('/dev/ttyS0',baud,timeout=1)
time.sleep(1)

#print("Processing serial communication...")
arduino.write(b'\n')
arduino.flush()
while(True):
    line = arduino.readline()
    while(len(line)>0 and not line[0] == '\n'):
       #if not line == val:
       #    print line[:-1],
       if line[0] == '>' or line[0] == '\r':
           print line[:-1],
       else:
           print(line[:-1])
       #print line[:-1],
       arduino.flush()
       #print(line)
       #sys.stdout.write(line[:-1])
       #sys.stdout.flush()
       #logging.debug(line[:-1])
       logging.debug(line)
       line = arduino.readline()
    val = raw_input("")
    if len(val)>0:
        #if val[0] == 'q':
        if val == 'quit':
           print("bye")
           arduino.close()
           sys.exit(0)
        arduino.write(val)
        logging.debug(val)
        line = arduino.readline()
    arduino.write(b'\n')
    arduino.flush()

arduino.close()
