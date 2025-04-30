import random
import script
possibleInputs = ["rock", "paper", "scissors"]
winner = {"rock" : "scissors", "paper" : "rock", "scissors" : "paper"}
compScore = 0
playerScore = 0

name = input("Enter your name: ")
scores = script.Scores()
# print(scores.findPlayer(name))
scores.addPlayer(name)
while (True):
    user = input("Enter your choice: ")
    comp = random.choice(possibleInputs)
    if (winner.get(user) == comp):
        print(comp)
        print("Player wins!")
        scores.addScore(name, 1)
        playerScore += 1
    elif (winner.get(comp) == user):
        print(comp)
        print("Computer wins!")
        compScore += 1
        scores.addScore(name, -1)
    elif user == comp:
        print(comp)
        print("Tie!")
        scores.addScore(name, 0)
    else:
        break
print("Player score: " + str(playerScore))
print("Computer score: " + str(compScore))