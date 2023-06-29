#!/usr/bin/env python3

#for loop
productList = ["card", "paper", "glue", "pencil"]
for product in productList:
  print(product)

#range function parameters have a starting and ending number
for counter in range(0,10):
    print("Counter is set to:",counter)
    if counter%2 == 0:
        print(counter,"is divisible by 2")
