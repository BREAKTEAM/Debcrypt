#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from passlib.hash import bcrypt
from libs import pingo
from colored import fg
import sys

color = fg('#008000')

print(color + "\n*************************************************")
print(color + "Debcrypt - Password cracker tools for bcrypt hash")
print(color + "*************************************************")
options = input(color + '\nYou want to crack? y/n: ')

if (options == "n"):
    sys.exit()
elif (options != "y" and options != "n"):
    sys.exit(color + 'Invalid Option')

passwords = (options == "y")
text_file = open("pass.txt", "r", encoding="cp437")

words = text_file.read().splitlines()

hash = input(color + 'Hash to crack: ')
length = len(words)

correct_word = ""
found = 0
for (index, word) in enumerate(words):
    pingo(index, length, prefix='Wait:', suffix='Words complete from the list')
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        found += 1
        break

if (found == 1):
    print(color + "\n\nPassword found!")
    print(color + "Results:", correct_word)
else:
    print(color + "\n\nUnfortunately, password not found.")
