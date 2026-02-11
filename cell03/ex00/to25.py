#!/usr/bin/env python

print("Enter a number less than 25")
start = int(input())

if start > 25:
    print("Error")
for i in range(start,26):
    print("Inside the loop, my variable is",i)