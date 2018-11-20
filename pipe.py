#!/usr/bin/env python

#from subprocess import *

#process = Popen(['rec', '-d', '-c1', '-r16000', 'output.wav'], stdout=PIPE, stderr=PIPE)
#stdout, stderr = process.communicate()
#print stdout
#Popen.wait()

import time

from subprocess import Popen, PIPE

def run(command):
    process = Popen(command, stdout=PIPE, stdin=PIPE, shell=True)
    while True:
        try:
            line = process.stdout.readline().rstrip()
            if not line:
                break
            print line
        except KeyboardInterrupt:
            pass
    return line

def runSleep(command):
    time.sleep(15)
    process = Popen(command)

if __name__ == "__main__":
    #pipe.run('/home/carlos/TFG_Carlos/iatros-run')

    try:
        for path in run(raw_input("Write your command to pipe down: ")):
            print path
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
