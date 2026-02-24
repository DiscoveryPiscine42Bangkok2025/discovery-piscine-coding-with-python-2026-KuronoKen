#!/usr/bin/env python

import sys

length = len(sys.argv)
if length > 1:
    print(f'parameters: {length-1}')
    for i in sys.argv[1:]:
        print(f'{i}: {len(i)}')
else:
    print("none")
