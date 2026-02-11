#!/usr/bin/env python

import sys

if len(sys.argv) == 1:
    for i in range(0,11):
        print(f'Table de {i}: ',end="")
        for j in range(0,11):
            print(i*j,end=" ")
        print()
else:
    print("none")