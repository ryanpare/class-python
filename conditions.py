#!/usr/bin/env python3

temperature = 82
if temperature > 0 :
  print('temperature is positive')

num1 = 1
num2 = 2

# AND
print("\nAND")
if num1 == 0 and num2 == 0:
  print('A is False, B is False: True')
else:
  print('A is False, B is False: False')

if num1 == 0 and num2 == 2:
  print('A is False, B is True: True')
else:
  print('A is False, B is True: False')

if num1 == 1 and num2 == 0:
  print('A is True, B is False: True')
else:
  print('A is True, B is False: False')

if num1 == 1 and num2 == 2:
  print('A is True, B is True: True')
else:
  print('A is True, B is True: False')

# OR
print("\nOR")
if num1 == 0 or num2 == 0:
  print('A is False, B is False: True')
else:
  print('A is False, B is False: False')

if num1 == 0 or num2 == 2:
  print('A is False, B is True: True')
else:
  print('A is False, B is True: False')

if num1 == 1 or num2 == 0:
  print('A is True, B is False: True')
else:
  print('A is True, B is False: False')

if num1 == 1 or num2 == 2:
  print('A is True, B is True: True')
else:
  print('A is True, B is True: False')