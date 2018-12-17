#!/usr/bin/python
# -*- coding: utf-8 -*-

#import sys
import time
import serial
import readline
import os
import argparse
#import os.path
from pathlib import Path


#Self dependencies
import read
import parse
import translate
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
     time.sleep(4)
     print s

     print ("Esta esperando: %s bytes" % ser.inWaiting())


     #os.remove('/home/carlos/TFG_Carlos_Defensa/kk.wav')
     #os.remove('/home/carlos/TFG_Carlos_Dtranscribeefensa/kk.raw')
     #os.remove('/home/carlos/TFG_Carlos_Defensa/kk.CC')

     while True:

         os.system("/home/carlos/TFG_Carlos_Defensa/iatros-run &")

         try:

             startCycle = time.time()
             # Recorder
             print "\nVERBOSE Recorder sox -d -c 1 -r 16000 kk.wav"
             pipe.run('sox -d -c 1 -r 16000 kk.wav')
             startCycle = time.time()


             # .wav -> .raw -> .cc -> IATROS-RUN
             start = time.time()
             print "\nVERBOSE .wav -> .raw"
             print "Status -", bash.run('/home/carlos/TFG_Carlos_Defensa/wav2raw')
             end = time.time()
             print "Time -", end - start

             start = time.time()
             print "\nVERBOSE .raw -> CC"
             print "Status -", bash.run('/home/carlos/TFG_Carlos_Defensa/raw2CC')
             end = time.time()
             print "Time -", end - start

             start = time.time()
             print "Esperando transcripcion iAtros /tmps/cops.out..."

             #Waits for /tmp/cops.out to exists (recognition is done)
             while True:
                 my_file = Path(file_name)
                 if my_file.is_file():
                     # file exists:
                     break
             end = time.time()
             print "Time ASR-", end - start

             start = time.time()
             print "\nVERBOSE Readidng '/tmp/cops.out'..."
             iatrosSCmd = read.main(file_name)
             end = time.time()
             print "Time -", end - start

             start = time.time()
             print "\nVERBOSE Processing text..."
             natSCmd = parse.main(iatrosSCmd)
             end = time.time()
             print "Time -", end - start

             start = time.time()
             print "\nVERBOSE Translating command: %s..." % natSCmd
             SCmd = translate.main(natSCmd)
             end = time.time()
             print "Time -", end - start

             input = SCmd + "\r\n"

             print "\nVERBOSE Sending: ", input
             ser.write(input)
             endCycle = time.time()
             print "Tiempo total ASRS for command despues de escribir en el puerto - ", endCycle - startCycle

             raw_input("Press Enter to continue...")
             ser.write("S\r")

         except Exception as e:
             print "Error type -", e
             raw_input("\nPress Enter to continue...")

     print "Cerrar"
