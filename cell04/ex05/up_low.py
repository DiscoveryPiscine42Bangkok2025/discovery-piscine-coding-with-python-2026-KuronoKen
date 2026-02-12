#!/usr/bin/env python

string = input()
for c in string:
    if c.isupper():
        print(c.lower(),end="")
    else:
        print(c.upper(),end="")
print()
