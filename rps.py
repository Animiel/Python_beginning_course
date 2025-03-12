import sys          # imports systeme module to use variables or functions to interact with the interpreter
import random           # imports random module to use some randomizing methods
from enum import Enum           # imports only one of the modules tools

# making a rock, leaf, scissors game

# intro to user input

# value = input("Please enter a value : \n")          # Waits for user to type anything -> result will always be string
# print(value)
# print(type(value))



# the game project

def play_rps():
    class RPS(Enum):
        ROCK = 1
        LEAF = 2
        SCISSORS = 3

    playerChoice = input("\nEnter...\n1 for Rock,\n2 for Leaf, or \n3 for Scissors :\n\n")

    if playerChoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3 please.")
        return play_rps()

    player = int(playerChoice)          # player could use like "one" or anything else but controling the input will be seen later

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Computer chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You won ! 🎉")
    elif player == 2 and computer == 1:
        print("🎉 You won ! 🎉")
    elif player == 3 and computer == 2:
        print("🎉 You won ! 🎉")
    elif player == computer:
        print("🤷‍♂️ Nobody wins. 🤷‍♂️")
    else:
        print("🥺 You lost... 🥺")
    
    print("\nPlay again ?")

    while True:
        playAgain = input("\nY for Yes or \nN for No \n")
        if playAgain.lower() not in ["y","n"]:
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print("❤️ Thanks for playing ! ❤️")
        sys.exit("Bye ! 🙋‍♂️")

play_rps()