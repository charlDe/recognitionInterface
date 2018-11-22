#!/usr/bin/python
# -*- coding: utf-8 -*-

#import sys
import time
import serial
import readline
import os
#import os.path
from pathlib import Path


#Self dependencies
import read
import parse
import transcribe
import pipe
import bash

#Testing flow
from subprocess import Popen, PIPE

#Conf: file_name
file_name = "/tmp/cops" + ".out"

#Port Listening
#python -m serial.tools.miniterm COM4

#Defining constants
STOPSBITS_ONE = serial.STOPBITS_ONE
EIGHTBITS = serial.EIGHTBITS
PARITY_NONE = serial.PARITY_NONE

with serial.Serial(port="/dev/rfcomm0", baudrate=9600   ,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPSBITS_ONE, timeout=0, xonxoff=False,
        rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None,
        exclusive=None) as ser:

     #print ser.inWaiting()
     print ("Bluetooth SPP serial port %s" % ser.name)
     s = ser.read(45)        # read up to ten bytes (timeout)
     print s

     #ser.flushInput()

     #ConfigDialog Data
     #print ("CTS: %s" % ser.cts)
     #print ("RTS: %s" % ser.rts)

     #print ("DSR: %s" % ser.dsr)
     #print ("DTR: %s" % ser.dtr)

     #print "Is Open?: %s" % ser.isOpen()
     #print ser.parity
     #print "\n"

     print ("Esta esperando: %s bytes" % ser.inWaiting())

     try:

         os.remove('/home/carlos/TFG_Carlos/kk.wav')
         os.remove('/home/carlos/TFG_Carlos/kk.raw')
         #os.remove('/home/carlos/TFG_Carlos/kk.CC')

         os.system("/home/carlos/TFG_Carlos/iatros-run &")

         while True:

             # Recorder
             print "\nVERBOSE Recorder sox -d -c 1 -r 16000 kk.wav"
             pipe.run('sox -d -c 1 -r 16000 kk.wav')

             #process = Popen('/home/carlos/TFG_Carlos/raw2CC')

             # .wav -> .raw -> .cc -> IATROS-RUN
             print "\nVERBOSE .wav -> .raw"
             print "Status -", bash.run('/home/carlos/TFG_Carlos/wav2raw')

             print "\nVERBOSE .raw -> CC"
             print "Status -", bash.run('/home/carlos/TFG_Carlos/raw2CC')

             print "Esperando transcripcion iAtros /tmps/cops.out..."

             while True:
                 my_file = Path(file_name)
                 if my_file.is_file():
                     # file exists:
                     break

             print "\nVERBOSE Readidng '/tmp/cops.out'..."
             iatrosSCmd = read.main(file_name)

             print "\nVERBOSE Processing text..."
             natSCmd = parse.main(iatrosSCmd)

             print "\nVERBOSE Transcribing order: %s..." % natSCmd
             SCmd = transcribe.main(natSCmd)

             print SCmd

             input = SCmd + "\r\n"
             #input = 'L 1011\n\r'
             print "\nVERBOSE Sending: ", input
             ser.write(input)
             #ser.flush()
             raw_input("Press Enter to continue...")

     except Exception as e:
         print "Error type -", e
         raw_input("\nPress Enter to continue...")

     print "Cerrar"
