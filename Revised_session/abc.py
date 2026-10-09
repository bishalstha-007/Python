# for random interger numbers
# number = random.randint(1,10 )

# for random floating point
# number = random.random()
# print(number)

import random

low = 10        # lowest value
high = 1000     # highest value
answer = random.randint(low, high)      # random generated value
guesses = 0     # starting guess
is_running = True

print("Number Guessing Game ")
print(f"Select a number between {low} and {high} \n")

while is_running:

    guess = input("Enter your guess: ")
    if guess.isdigit():            # making sure that the guesses number is of integer value
        guess = int(guess)         # converting into integer value
        guesses += 1               # for counting number of guesses number

        if guess < low or guess > high:
            print("That number is out of range")
            print(f"Please select a number between {low} and {high}")

        elif guess < answer:
            print("Too Low ! Try again!")
        elif guess > answer:
            print("Too High! Try again!")

        else:
            print(f"Correct! the answer was {answer}")
            print(f"Number of guesses:{guesses}")  
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please Select a number between {low} and {high} \n")
