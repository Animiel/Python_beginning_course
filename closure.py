# Closure is a function accessing parent's scope after parent has returned

def parent(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")
    
    return play_game

tommy = parent("Tommy", 3)
jenny = parent("Jenny", 5)
tommy()
tommy()
jenny()