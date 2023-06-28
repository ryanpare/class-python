#!/usr/bin/env python3

smallNumber = 0
largeNumber = 100

while smallNumber != largeNumber:
  if smallNumber%2 == 0 :
      print(smallNumber, "divisible by 2")
  elif smallNumber%3 == 0 :
      print(smallNumber, "divisible by 3")
  elif smallNumber%5 == 0 :
      print(smallNumber, "divisible by 5")
  else :
      print(smallNumber, "not divisible by anything")
  smallNumber += 1