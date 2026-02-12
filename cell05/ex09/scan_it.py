#!/usr/bin/env python

import sys

y = sys.argv[1:]

if y == []:
    print("none")
else:
    print(y[0].upper())