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

#Conf: pseudo-semantic
SEmdDIC = {
    #semantics synonims...
}

REmdDIC = {
    #modulables
    "movimiento": ['anda','muevete','ve','camina','gira', 'moonwalker', 'crusaito', 'aletea', 'apoyate', 'menea'],
    #to extend... [cuantifiers] "muy feliz"
    #"expresion": ['feliz']
}

SCmdDIC = {

    #actions SCmd
    "S": [
        "stop",
        "para"
        ],
    #actions 2 SCmd
    "M": [
        "anda","muevete","ve","camina","gira","salta","moonwalker","swing","crusaito","aletea",
        "espera","apoyate","menea", "nervioso","excitado"
        ],

    #expresions SCmd
    "H": [
        "feliz","superfeliz","triste","somnoliento","pedorro","confundido",
        "enamorado","enfadado","miedoso","magico","ola","victorioso",
        "derrotado"
        ]
}

ActmdDIC = {
    #base stop cotrolSEmdSEmdDIC
    "para": "S",
    "stop": "S",

    #movements IDs
    "anda": [3,4,1,2],
    "muevete": [3,4,1,2],
    "ve": [3,4,1,2],
    "camina": [3,4,1,2],
    "gira": [3,4], #mod
    "salta": [5,11],
    "moonwalker": [6,7], #mod
    "swing": [8],
    "crusaito": [9,10], #mod
    "aletea": [12,13], #mod
    "espera": [14],
    "apoyate": [15,16], #mod
    "menea": [17,18], #mod
    "nervioso": [19],
    "excitado": [20],

    #to extend ... [cuantifiers] "muy feliz"
    #expressions IDs
    "feliz": [1],
    "superfeliz": [2],
    "triste": [3],
    "somnoliento": [3],
    "pedorro": [5],
    "confundido": [6],
    "enamorado": [7],
    "enfadado": [8],
    "miedoso": [9],
    "magico": [10],
    "ola": [11],
    "victorioso": [12],
    "derrotado": [13]
}

SCmdDICmod = {

    #direcciones
    "izquierda": 0,
    "derecha": 1,
    "delante": 2,
    "adelante": 2,
    "atras": 3,

    #cuantificadores
    "muy": 1,

    #"rapido": 1,
    #"lento": 1
}

# Given a two dimensional value listed dictionary
# and an element, returns the value list containing the element
# else, returns None
# @returns List containing the element
def returnListWichContains(element, DIC):
    keys = DIC.keys()
    for k in keys:
        if element in DIC[k]:
            return DIC[k]
    return None

def main(commandL):

    transcript = "" #full
    mod = "" #partial

    SCmdDICvalues = list(itertools.chain.from_iterable(SCmdDIC.values()))
    #print "\nSCmdDICvalues: ", SCmdDICvalues
    REmdDICvalues = list(itertools.chain.from_iterable(REmdDIC.values()))
    #print "REmdDICvalues: ", REmdDICvalues
    #SCmdDICmodvalues = list(itertools.chain.from_iterable(SCmdDICmod.values()))
    #print "SEmdDICvalues: ", SCmdDICmodvalues
    SCmdDICmodvalues = SCmdDICmod.keys()

    #REMIND: returns the key of value in SCmdDIC
    # SCmdDIC.keys()[SCmdDIC.values().index'gira', 'moonwalker', 'crusaito', 'aletea', 'apoyarse', 'menea'],(cmd)]


    #Each cmd appearance in DICs is a significative lexema to generate return
    modular = None
    for cmd in commandL:

        #print "\n" + cmd
        # process : [anda] hacia [adelante=delante]
        # result  : M 2 30 1000?

        # process Note: Directional modular can't be the verb alone
        # in Zowi's command language


        if cmd == "stop" or cmd == "para":
            transcript += "S"
            return transcript

        if cmd in SCmdDICvalues:
            # process S,M,H : M
            #print "\n" + cmd + " in SCmdDICvalues"
            transcript += SCmdDIC.keys()[SCmdDIC.values().index(returnListWichContains(cmd, SCmdDIC))]
            if cmd not in REmdDICvalues:
                modular = False
                #print "Not in"

        if cmd in REmdDICvalues:
            #print "\n" + cmd + " in REmdDICvalues and modular"
            # process movimiento : M modular?
            mod = cmd
            modular = True

        if cmd in SCmdDICmodvalues and modular:
            #print "\n" + cmd + " in SEmdDICvalues"
            # process direccion:
            #print SCmdDICmod[cmd]
            #print ActmdDIC[mod]
            add = str(ActmdDIC[mod][SCmdDICmod[cmd]])
            transcript += " " + add
        elif modular == False:
            #process not modular ID
            #print "\n" + cmd + " not modular"
            add = str(ActmdDIC[cmd][0])
            transcript += " " + add

        #else:
            #process

    return transcript

#print ActmdDIC["anda"]
#print SCmdDICmod["delante"]

#print type(ActmdDIC["anda"][SCmdDICmod["delante"]])
if __name__ == "__main__":

    input = ['apoyate','hacia','la','izquierda']

    print "Transcribe: ", input

    result = main(input)
    print "\nResultado: ", result
