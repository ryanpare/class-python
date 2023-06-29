#!/usr/bin/env python3

#for loop
productList = ["card", "paper", "glue", "pencil"]
for product in productList:
  print(product)

#range function parameters have a starting and ending number
for counter in range(0,10):
    print("Counter is set to:",counter)

#range function using third parameter to increment other than 1
#with the third parameter as -2 move through the range down increments of -2
for counter in range(10,1,-2):
    print("Counter is set to:",counter)

#loop through string
for char in "Python":
    print(char)