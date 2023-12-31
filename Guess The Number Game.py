# This could be a fun Python project for groups or events where a random generator is needed.
# It’s useful for conducting lotteries, board games, or just between players to guess a random number.
# Skills used: Getting familiar with the random function, variables, integers, print, if/else, and while loops.

# Skills to build this project:
# random module
# function
# variables
# intergers
# conditional statements
# loops

# START
# First, we import the "random moudle".
import random

# define a function for the code.
def guess():
    num_to_guess = random.randint(1, 100)
    print(num_to_guess)
    # User's name
    user_name = input("What is your name? ")
    print(f"\nWelcome {user_name.title()}, to GUESS THE NUMBER 🧐")
    # variable to keep count
    count = 0
    # Now for the loop.
    while True:
        start_or_stop = input("Enter 👌Yes / 👎No: ").lower()
        if start_or_stop == "yes":
            try:
                while True:
                    guess_number = int(input("\nEnter a number btw 1 - 100: "))
                    if guess_number == num_to_guess:
                        print(f"\n{guess_number} is correct.")
                        print(f"Well done {user_name.title()}, you did that in {count} try.")
                        if count > 5:
                            print(f"\nBravo {user_name.title()}👍, next time get your tries below 5 ")
                        else:
                            print(f"\nThat was exllecent {user_name.title()} 🌟")
                        break
                    elif guess_number > num_to_guess:
                        count += 1
                        print(f"\nIncorrect\nVaule too high")
                    else:
                        count += 1
                        print("\nIncorrect\nValue too low")
            except ValueError:
                count += 1
                print(f"Wrong value entered, {user_name.title()} 😒")
        elif start_or_stop == "no":
            print(f"Thanks for your time {user_name.title()}. Goodbye!")
            break
        else:
            print(f"Unknown value {user_name.title()} 😒. Try again!")

guess()


















