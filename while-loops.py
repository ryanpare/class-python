#!/usr/bin/env python3

#number countdown
myNumber = -4
while myNumber < 0:
  myNumber +=1
  if myNumber == 0:
    print(0)
    continue
  print('T'+ str(myNumber))
print('Blastoff!')

#string builder
textEntered = ""
stringBuilder = ""
while textEntered != "quit":
  textEntered = input("Enter in a string, enter quit to exit the loop:")
  if textEntered != "quit":
    stringBuilder += textEntered + " "
print(stringBuilder)

#loop break
myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    if myNumber == 2:
        break
    print(myNumber)
print('Blastoff!')

#loop continue
print("loop continue")
myNumber = 6
while myNumber > 0:
    myNumber = myNumber - 1
    if myNumber == 2:
        continue
    print(myNumber)
print('Blastoff!')