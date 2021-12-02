# CTI - 110
# P5LAB4
# Anthony Davis
# 18 Nov 2021

"""
Rock Paper Scissors. We will break this into many functions.
- play one round
- get player pick
- get cpu pick
- compare to find winner
"""
import random

def playOneRound():
    """plays one round of RPS
        input: none, returns: who won the round ("player" or "cup")
    """
    print ("Play one round.")
    winner = None
    player = getPlayerPick()
    cpu = getCpuPick()
    winner = whoWon(player, cpu)
    print ("player:", player, "\tcpu:", cpu)
    return winner

def getPlayerPick():
    choice = input("[rock/paper/scissors]? ")
    return choice

def getCpuPick():
    choices = ["rock", "paper", "scissors"]
    roll = random.randint (0, 2) # matches indexes of list above
    choice = choices[roll]
    return choice

def whoWon(player, cpu):
    """ The meat of the RPS program: find out who won.
    input: player pick, cpu pick
    returns: "player" or "cup" (the winner) """
    winner = None

    # 9 possible options --- player has 3 X cpu has 3
    if player == "rock":
        if cpu == "rock":
            winner = "it's a tie" # tie
        if cpu == "paper":
            winner = "cpu"
        if cpu == "scissors":
            winner = "player" # rock breaks scissors
    if player == "paper":
        if cpu == "paper":
            winner = "it's a tie" # tie
        if cpu == "rock":
            winner = "player" # paper beats rocks
        if cpu == "scissors":
            winner = "cpu"
    if player == "scissors":
        if cpu == "scissors":
            winner = "it's a tie" # tie
        if cpu == "paper":
            winner = "player" # scissors beats paper
        if cpu == "rock":
            winner = "cpu"


    return winner

def main():
    print("Rock Paper Scissors Game")
    playerWins = 0
    cpuWins = 0
    keepGoing = "y"
    while keepGoing == "y":
        winner = playOneRound()
        print ("winner is", winner)
        if winner == "player":
            playerWins += 1
        if winner == "cpu":
            cpuWins += 1
        print("SCORE: player", playerWins, "\tcpu:", cpuWins)
        keepGoing = input("again? (y/n) ")

# start program
if __name__ == "__main__":
    main()

