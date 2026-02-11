#!/usr/bin/env python

print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

num3 = num1*num2
print(num1,"x",num2,"=",num3)

if (num3 < 0):
    print("The result is negative.")
elif (num3 > 0):
    print("The result is positive.")
else:
    print("The result is positive and negative.")