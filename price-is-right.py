#!/usr/bin/env python3

itemPrice = 82
prompt = "What is the price of the item: "
guess = int(input(prompt))
nameContestant = "Ryan"

def getWinner(guess):
  if guess == itemPrice :
    print("Your guess of {0} is a great guess! You're spot on. \n Contestant is a Winner!".format(guess))
  elif guess > itemPrice :
    print("Your guess of {0} is over the price. Contestant is out of the game".format(guess))
  elif guess < itemPrice :
    print("Your guess of {0} is under the price. Contestant still in game".format(guess))

try:
  print("\n")
  getWinner(guess)
except ValueError as error :
  print('Oops, you did not enter a number')