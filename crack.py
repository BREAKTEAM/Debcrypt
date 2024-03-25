#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from passlib.hash import bcrypt
from libs import pingo
from colored import fg

color = fg('#008000')
color_err = fg("#FF0000")

def crack_bcrypt(wordlist: str, hash_to_crack: str) -> str:
    '''
    crack bcrypt using  bruteforce method
    Args:
        wordlist (str): Path to the wordlist file (opt).
        hash_to_crack (str): The hash to be cracked.

    Returns:
        str: The cracked password or None if not cracked.
    '''
    try:
        with open(wordlist, "r", encoding="cp437") as text_file:
            words = text_file.read().splitlines()

    except FileNotFoundError:
        print(color_err + "Error: Wordlist file is invalid!")
        sys.exit(1)

    except Exception as err:
        print(color_err + f"Error: {err}")
        sys.exit(1)

    length = len(words)
    for index, word in enumerate(words):
        pingo(index, length, prefix='Wait:', suffix='Words complete from the list')
        if bcrypt.verify(word, hash_to_crack):
            return word

    return None

def main():
    print(color + "\n*************************************************")
    print(color + "Debcrypt - Password cracker tools for bcrypt hash")
    print(color + "*************************************************\n")

    # user can specify a wordlist as cmdline arg if they want.
    # uses pass.txt as default if the user didnt provide.
    if len(sys.argv) > 1:
        wordlist = sys.argv[1]
    else:
        wordlist = "pass.txt"

    # take userinp in consistence manner
    options = input(color + '\nDo you want to crack? (y/n): ').strip().lower()
    if options != "y":
        sys.exit()

    hash = input(color + 'Enter the hash to crack: ').strip()

    if not hash:
        print(color_err + "Error: Hash cannot be empty.")
        sys.exit(1)


    cracked = crack_bcrypt(wordlist, hash)

    if cracked:
        print(color + "\n\nPassword found!")
        print(color + "Result:", cracked)
    else:
        print(color_err + "\nUnfortunately, password not found.")

if __name__ == "__main__":
    main()
