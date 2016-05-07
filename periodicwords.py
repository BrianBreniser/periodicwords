#!/usr/bin/env python

from __future__ import print_function
from sys import argv

words = open('/usr/share/dict/words')
adictionary = words.readlines()
words.close()

dictionary = map(lambda x: x[:-1], adictionary)

periodicTable = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'C', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Ti', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sd', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo']

def doitwrapper(word):
    originalword = word
    word = word.lower()

def doitrecursively(periodicsymbol, word):
    if word.startswith(periodicsymbol.lower()):
        word = word.replace(periodicsymbol.lower(), '', 1)
        # return largest string containing all of the next periodic table of elements
        # create a new list recursively with all the new answers
        # find the largest one
        # return that one
    else:
        return ''

def doit(word):
    word = word.lower()
    originalword = word
    answer = ""

    while word != "":
        used = 0
        for i in periodicTable:
            # print "trying " + i
            if word.startswith(i.lower()):
                # print "found that " + i + " is in the word!"
                answer += i
                used = 1
                word = word.replace(i.lower(), '', 1)

        if word == "":
            print(originalword + ": " + answer)
            return

        # only get here if word is not done and we didn't make any changes
        if used == 0:
            return

if len(argv) <= 1:
    for i in dictionary:
        doit(i)

if len(argv) > 1:
    for i in argv[1:]:
        doitwrapper(i)
