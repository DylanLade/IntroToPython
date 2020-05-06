import random
import pickle
import sys


def botRPS():
    bot = random.randint(1,3)
    return bot


def rpsGame(player, bot):
    if player == 1:
        playerChoice = "Rock"
        if bot == 2:
            botChoice = "Paper"
            result = 0
        if bot == 3:
            botChoice = "Scissors"
            result = 1
        if bot == 1:
            botChoice = "Rock"
            result = -1

    if player == 2:
        playerChoice = "Paper"
        if bot == 3:
            botChoice = "Scissors"
            result = 0
        if bot == 1:
            botChoice = "Rock"
            result = 1
        if bot == 2:
            botChoice = "Paper"
            result = -1

    if player == 3:
        playerChoice = "Scissors"
        if bot == 1:
            botChoice = "Rock"
            result = 0
        if bot == 2:
            botChoice = "Paper"
            result = 1
        if bot == 3:
            botChoice = "Scissors"
            result = -1

    if result == 0:
        wlt = "lose"
    if result == 1:
        wlt = "win"
    if result == -1:
        wlt = "tie"

    print("You chose " + playerChoice + ". The computer chose " + botChoice + ". You " + wlt + "!")
    return result


def savePlayer(player):
    with open(player["name"] + ".rps", 'w') as fp:
        fp.write(player["name"])
        fp.write('\n')
        fp.write(str(player["win"]))
        fp.write('\n')
        fp.write(str(player["loss"]))
        fp.write('\n')
        fp.write(str(player["ties"]))


def loadPlayer(name):
    player = dict()
    with open(name + ".rps", "r") as fp:
        player["name"] = (fp.readline()).rstrip()
        player["win"] = int(fp.readline())
        player["loss"] = int(fp.readline())
        player["ties"] = int(fp.readline())

    return player


def stats(player):
    print(player["name"] + ", here are your gameplay statistics...")
    print("Wins: " + str(player["win"]))
    print("Losses: " + str(player["loss"]))
    print("Ties: " + str(player["ties"]))
    wl = player["win"]/player["loss"]
    print("Win/Loss Ratio: " + str(round(wl, 2)))
    print()


def Game(player, roundNumber):
    print("Round " + str(roundNumber) + "\n")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors\n")

    choosing = True 
    while(choosing):
        try:
            playerRPS = int(input("What will it be? "))
            if(playerRPS in range(1,4)):
                choosing = False
                break
            print("Please select a valid option")
            choosing = True
        except ValueError:
            print("Please enter a numeric value")
            choosing = True

    result = rpsGame(playerRPS, botRPS())

    if result == 1: # Win
        player["win"] += 1
    if result == 0: # loss
        player["loss"] += 1
    if result == -1: # Tie
        player["ties"] += 1

    roundNumber = roundNumber + 1
    return roundNumber


def createPlayer(player, name):
    player["name"] = name
    player["win"] = 0
    player["loss"] = 0
    player["ties"] = 0

    return player


def playMenu(player, roundNumber):

    print("What would you like to do?\n")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit\n")

    choosing = True 
    while(choosing):
        try:
            choice = int(input("Enter Choice: "))
            if(choice in range(1,4)):
                choosing = False
                break
            print("Please select a valid option")
            choosing = True
        except ValueError:
            print("Please enter a numeric value")
            choosing = True

    if choice == 1:
        roundNumber = Game(player, roundNumber)
    if choice == 2:
        stats(player)
    if choice == 3:
        savePlayer(player)
        sys.exit(0)

    return roundNumber


def main():

    player = dict()
    start = 1
    roundNumber = 1

    while(1):
        if start == 1:
        
            print("Welcome to Rock, Paper, Scissors!\n")
            print("1. Start New Game")
            print("2. Load Game")
            print("3. Quit\n")

            choosing = True 
            while(choosing):
                try:
                    choice = int(input("Enter Choice: "))
                    if(choice in range(1,4)):
                        choosing = False
                        break
                    print("Please select a valid option")
                    choosing = True
                except ValueError:
                    print("Please enter a numeric value")
                    choosing = True
        
            if choice == 1:
                name = input("What is your name? ")
                print("Hello "+ name + " Let's Play!")
                player = createPlayer(player, name)
                start = 0

            if choice == 2:
                name = input("What is your name? ")
                player = loadPlayer(name)
                start = 0

            if choice == 3:
                print(player)
                sys.exit(0)
        
            roundNumber = Game(player, roundNumber)

        else:
            roundNumber = playMenu(player, roundNumber)

if __name__ == "__main__":
    main()