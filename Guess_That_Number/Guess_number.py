# This is a guess the number game.

import random
name = input("Hello, What is your name? \n")
age = int(input("Please Enter your Age :- \n"))
secret_number = random.randint(1, age)

print("Now, {} I am thinking of a number which should be in range 1 and {}.".format(name, age))

guesses = 1
print("Take a Guess.")

while True:
    guess = int(input())
    if guess > secret_number:
        print("Your Guessed Number is too high! Try Again")
    elif guess < secret_number:
        print("Your Guessed Number is too low! Try Again")
    else:
        break
    guesses += 1

print("Congratulations! You have guessed the correct number in {} guesses".format(guesses))
