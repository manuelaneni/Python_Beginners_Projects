"""
Rock, Paper, Scissors Game
One of the most beloved games of all-time and a simple Python project to test your skills.
Start by making it player vs computer.
"""
# To complete we need:
# Random Module
# Loops
# Conditional statments

import random
def game():
    print("Welcome to Rock 🪨, Paper 📜", "Scissor ✂️")
    player = input("\nPlease enter your name: ").title()
    computer = "AI"
    # variables needs to fulfil condition
    count = 0
    player_score = 0
    ai_score = 0


    # loop

    while True:
        lst = ["rock", "paper", "scissor"]
        ai_choice = random.choice(lst)
        # print(ai_choice)
        # Player's' input

        user = input("Enter 'rock, paper, scissor': ")
        if user == ai_choice:
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("Draw")
        elif user =="rock" and ai_choice == "paper":
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("AI wins")
            ai_score += 1
        elif user =="scissor" and ai_choice == "rock":
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("AI wins")
            ai_score += 1
        elif user =="paper" and ai_choice == "scissor":
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("AI wins")
            ai_score += 1
        elif user == "paper" and ai_choice == "rock":
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("Player wins")
            player_score += 1
        elif user == "rock" and ai_choice == "scissor":
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("Player wins")
            player_score += 1
        elif user == "scissor" and ai_choice == "paper":
            print(f"{player}: {user}"
                  f" | {computer}: {ai_choice}")
            print("Player wins")
            player_score += 1
        count += 1


        if count == 3:
            if player_score > ai_score:
                print(f"Player wins: {player_score} AI score: {ai_score}")
            elif player_score == ai_score:
                print(f"DRAW"
                      f"\nPlayer's score: {player_score} AI score: {ai_score}")
            else:
                print(f"AI wins {ai_score}, Player's score: {player_score}" )
            print(f"Thanks for playing.")
            break


game()

