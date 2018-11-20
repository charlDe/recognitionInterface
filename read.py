#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import itertools
import datetime
import os

#f_name = raw_input("Introduce el nombre del archivo: ")

#Conf: file_name
file_name = "/tmp/cops" + ".out"

#EASING IO
def logging(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def escribir():
    #SRAH behaveourdef logging(filename, line):
    with open(filename, 'r+logging') as f:
        content = f.read()
        f.seek(0, 0)
        f.writ(line.rstrip('\r\n') + '\n' + content)
    file = open(file_name, "w+")
    for i in range(10):
        file.write("Zowi, command number %d\r\n" % (i+1))
    file.close()

def main():
    #Date info for LOG
    date = datetime.datetime.now().strftime("%y-%m-%d %H:%M")

    f = open(file_name, "r")
    file = f.readline()
    # En log
    print "\n#En log#"
    print date
    line = file.strip("\n")
    print line + '\n'
    logging("readingFile/log.txt", date + " " + line)
    f.close()
    borrar(file_name)
    return file.strip("\n")

def borrar(file_name):
    os.remove(file_name)


if __name__ == "__main__":
    if file_name == "readingFile/log.txt":
        print "Can't overwrite log"
        exit()
    else:

        print "E L S E"
        # SRAH Behavour
        # print ("Escribiendo el archivo... %s \n" % file_name)
        # escribir()

        # Leer ordenes - Append LOG
        # print "\nLeyendo el archivo..."
        # orden = leer()
        # print "\n" + orden

        # Parseando
        # print "\nProcesando texto ..."
        # transcription = parse(orden)
        # print transcription
        # time.sleep(5)

        # Transcribiendo
        # print "\nTrancribiendo ..."
        # command = transcribe(transcription)
        # print command

        # Delete
        # print "\nBorrando el archivo el archivo...\n"
        # borrar(file_name)
