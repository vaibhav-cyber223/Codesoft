#Rock,Paper,Sizor Game
import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors: ")
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("Computer wins!")

    Replay = input("Play again? (yes/no): ")
    if Replay != "yes":
        break
