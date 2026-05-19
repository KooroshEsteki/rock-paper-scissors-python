import random

def main():
    options = ["rock", "paper", "scissors"]

    computer = random.choice(options)

    player = input("Choose rock, paper, or scissors: ").lower()

    if player not in options:
        print("Invalid input. Please choose rock, paper, or scissors.")
        return

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")

main()
