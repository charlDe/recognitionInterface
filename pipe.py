#!/usr/bin/env python

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

    try:
        for path in run(raw_input("Write your command to pipe down: ")):
            print path
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
