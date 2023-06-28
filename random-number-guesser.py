#!/usr/bin/env python3

#module to generate random numbers
import random

#create a random number between 1 and 20
#and assign it to randomNumber
randomNumber = random.randrange(1, 20)

#variable for number or guesses
numberOfGuesses = 1

#ask the user to input a number between 1 and 20
guess = int(input("Guess a number between 1 to 20: "))

#loop which will keep going until the number is guessed
while guess != randomNumber:
    #increment the number of numberOfGuesses by 1 each time
    numberOfGuesses += 1
    if guess > randomNumber:
        print(guess, "is too high")
        guess = int(input("Guess a lower number: "))
    elif guess < randomNumber:
        print(guess, "is too low")
        guess = int(input("Guess a higher number: "))
    else:
        print("You got the number ", randonNumber)

print("You guessed correctly in", numberOfGuesses, "attempts!")