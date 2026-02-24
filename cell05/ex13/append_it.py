#!/usr/bin/env python

import sys

param = sys.argv[1:]

if param:

    for i in param:
        if not i.endswith("ism"):
            print(i+"ism")
else:
    print("none")