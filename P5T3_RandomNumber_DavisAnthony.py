# CTI - 110
# P5T3 - Random Numbers
# Anthony Davis
# 16 Nov 2021

# Write a few random number generators for common uses.
# to use random:
import random
# diceRoll = random.randint(1, 6) # example

def rollD6():
    """ input: none. output : int from 1 to 6. """
    roll = random.randint(1, 6)
    return roll

def roll2D6():
    roll = rollD6() + rollD6()
    return roll

def coinFlip():
    """input: none. output: a string, "heads" or "tails" """
    sides = ["heads", "tails"]
    flip = random.randint(0, 1)
    return sides[flip]

def RPS():
    """
    Rock paper scissors choice.
    Input: none Output: a string, "rock", "paper", or "scissors"
    """
    choice = random.randint(1, 3)
    hand = None # this will be the RPS hand
    if choice == 1:
        hand = "rock"
    elif choice == 2:
        hand = "paper"
    elif choice == 3:
        hand = "scissors"
    return hand


def main():
    # a set seed means these are always the same
    # random.seed(42)
    print("Rolling dice...")
    for num in range(10):
        roll = rollD6()
        print (roll, end=" ")
    print()
    print("Rolling 2 dice...")
    for num in range(10):
        roll = roll2D6()
        print(roll, end=" ")
    print()
    print()
    print("Flipping a coin...")
    for num in range(5):
        flip = coinFlip()
        print(flip, end=" ")
    print()
    print()
    print("Playing rock, paper, scissors...")
    for num in range(5):
        myHand = RPS()
        yourHand = RPS()
        print("Me:" ,myHand, "vs You:", yourHand)
    




# start program
main()
