import sys          # imports systeme module to use variables or functions to interact with the interpreter
import random           # imports random module to use some randomizing methods
from enum import Enum           # imports only one of the modules tools

class RPS(Enum):
    ROCK = 1
    LEAF = 2
    SCISSORS = 3


# making a rock, leaf, scissors game

# intro to user input

# value = input("Please enter a value : \n")          # Waits for user to type anything -> result will always be string
# print(value)
# print(type(value))



# the game project

print("")
playerChoice = input("Enter...\n1 for Rock,\n2 for Leaf, or \n3 for Scissors :\n\n")

player = int(playerChoice)          # player could use like "one" or anything else but controling the input will be seen later

if player < 1 or player > 3:
    #print("You must enter 1, 2, or 3.")         # this wouldn't stop the program from running so it would continue with a non desirable value
    sys.exit("You must enter 1, 2, or 3 please.")
computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Computer chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")

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