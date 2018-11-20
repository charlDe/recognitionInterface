#!/usr/bin/python
# -*- coding: utf-8 -*-

#EASING parsing
def main(orden):
    orden = orden[3:-4]
    orden = orden.replace("<sil>", "")
    ordenL = orden.split()
    return ordenL
