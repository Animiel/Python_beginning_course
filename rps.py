import sys          # imports systeme module to use variables or functions to interact with the interpreter
import random           # imports random module to use some randomizing methods
from enum import Enum           # imports only one of the modules tools

# making a rock, leaf, scissors game

# intro to user input

# value = input("Please enter a value : \n")          # Waits for user to type anything -> result will always be string
# print(value)
# print(type(value))



# the game project
def rps(name="player1"):
    gameCount = 0
    playerWins = 0
    cpuWins = 0

    def play_rps():
        nonlocal name
        nonlocal playerWins
        nonlocal cpuWins
        class RPS(Enum):
            ROCK = 1
            LEAF = 2
            SCISSORS = 3

        playerChoice = input(f"\n{name}, please enter...\n1 for Rock,\n2 for Leaf, or \n3 for Scissors :\n\n")

        if playerChoice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1, 2, or 3 please.")
            return play_rps()

        player = int(playerChoice)          # player could use like "one" or anything else but controling the input will be seen later

        computerChoice = random.choice("123")
        computer = int(computerChoice)

        print(f"\n{name} chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Computer chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal playerWins
            nonlocal cpuWins

            if player == 1 and computer == 3:
                playerWins += 1
                return f"🎉 {name} won ! 🎉"
            elif player == 2 and computer == 1:
                playerWins += 1
                return f"🎉 {name} won ! 🎉"
            elif player == 3 and computer == 2:
                playerWins += 1
                return f"🎉 {name} won ! 🎉"
            elif player == computer:
                return "🤷‍♂️ Nobody wins. 🤷‍♂️"
            else:
                cpuWins += 1
                return f"🥺 {name} lost... 🥺"
        
        gameResult = decide_winner(player, computer)
        print(gameResult)

        nonlocal gameCount
        gameCount += 1

        print(f"\nGame count : {gameCount}")
        print(f"\n{name}'s wins : {playerWins}")
        print(f"\nComputer wins : {cpuWins}")
        
        print(f"\nPlay again, {name} ?")

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
            sys.exit(f"Bye {name} ! 🙋‍♂️")

    return play_rps         # without () -> only to call function

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description = "Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar = "name",
        required=True, help="The name of the person to play the game."
    )

    args = parser.parse_args()
    rockPaperScissors = rps(args.name)
    rockPaperScissors()