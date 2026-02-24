#!/usr/bin/env python

from sys import argv

def main():
    if not len(argv) > 1:
        print("none")
        return
    keyword = argv[1]
    if input("What was the parameter? ") == keyword:
        print("Good job")
    else:
        print("Nope, sorry...")

main()