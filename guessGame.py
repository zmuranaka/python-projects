# File: guessGame.py
# Zachary Muranaka
# Allows the user to play a simple, text-based number guessing game

from random import randint

print("I am going to generate a random number from 1 to...")

try:
    maxNum = int(input())
    generatedNum = randint(1, maxNum)

    numberOfGuesses = 0

    while True:
        print("What is your guess?")
        currentGuess = int(input())
        numberOfGuesses += 1
        if(currentGuess == generatedNum):
            break
        elif(currentGuess < 1 or currentGuess > maxNum):
            print("That number is not within the range")
        elif(currentGuess < generatedNum):
            print("Guess higher.")
        else:
            print("Guess lower.")

    print("Correct! It took you", numberOfGuesses, "guesses.")
    print("{0} / 2^{1} = {2}".format(maxNum, numberOfGuesses, (maxNum / (2 ** numberOfGuesses))))
except ValueError:
    print("Positive integers only please")
