# CTI - 110
# P5LAB3 - Coin Flip
# Anthony Davis
# 18 Nov 2021

# we will start off with a coin flip, then do
# rock, paper, scissors.

import random

def coinFlip():
    """returns: "heads" or "tails" """
    result = None # inc ase no if statement fires
    flip = random.randint(0,1)
    if flip == 0:
        result = "heads"
    if flip == 1:
        result = "tails"

    return result



def countFlips():
    # to start off, let's just count heads and tails
    numHeads = 0
    numTails = 0
    numTries = int(input("How many coin flips? "))
    for count in range(numTries):
        flip = coinFlip()
        if flip == "heads":
            numHeads += 1
        if flip == "tails":
            numTails += 1
    print(numTries, "flips: heads=", numHeads, "tails=", numTails)

def callTheCoin():
    """ The "call it in the air" minigame
        input: none
        return: none (might change this later)
    """
    # ask the user to call the flip
    choice = input("Call it (heads/tails): ")

    # flip the coin
    flip = coinFlip()

    # compare -- did they call it correctly?
    """
    # the easy way
    if choice == flip:
        print("You called it! It was", flip)
    else:
        print("Nope, it was", flip)
    """
    # the hard way:
    winner = None
    if choice == "heads":
        if flip == "heads":
            winner = "player"
        if flip == "tails":
            winner = "cpu"
    if choice == "tails":
        if flip == "heads":
            winner = "cpu"
        if flip == "tails":
            winner = "player"
    print ("You called", choice, "the flip was", flip)
    print ("Winner is:", winner)
        

def main():
    
    # countFlips()
    keepGoing = "y"
    while keepGoing == "y":
        callTheCoin()
        keepGoing = input("Again? (y/n): ")


# start program
if __name__ == "__main__":
    main()
