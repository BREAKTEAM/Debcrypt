#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from passlib.hash import bcrypt
from libs import pingo
import os
import sys

options = input('You want crack? y/n ')

if (options != "y" and options != "n"):
    sys.exit('Invalid Option')

passwords = (options == "y")
text_file = open("pass.txt", "r")

words = text_file.read().splitlines()

hash = input('hash to crack: ')
length = len(words)

correct_word = ""
for (index, word) in enumerate(words):
    pingo(index, length, prefix='Wait:', suffix='Complete')
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        print()
        break

print("Results:", correct_word)
