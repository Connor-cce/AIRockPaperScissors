import random
from script import Scores
from markov import predictor

choices = ["rock", "paper", "scissors"]
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

name = input("Enter your name: ").strip()
scores = Scores()
scores.addPlayer(name)

player, computer = 0, 0
arr = scores.getArray(name)
rock = arr[0]
paper = arr[1]
scissors = arr[2]
decision_maker = predictor(rock, paper, scissors)

def decision(move):
    if move == 'rock': return "paper"
    elif move == 'paper': return 'scissors'
    else: return 'rock'

while True:
    user = input("Enter rock, paper, scissors (or anything else to quit): ").strip()
    if user not in choices:
        break

    comp = decision(decision_maker.nextMove(user))
    print("Computer chose:", comp)

    if beats[user] == comp:
        print("You win!")
        scores.addScores(name, 1)
        player += 1
    elif beats[comp] == user:
        print("Computer wins!")
        scores.addScores(name, -1)
        computer += 1
    else:
        print("It's a tie!")
        scores.addScores(name, 0)

print(f"Final — You: {player}, Computer: {computer}")

#create a variable that stores the new 2d array of scores
new_scores = decision_maker.getMark()
#create three string variables that store each of the columns values
new_r = "?, ?, ?", (new_scores[0][0],new_scores[0][1],new_scores[0][2])
new_p = "?, ?, ?", (new_scores[1][0],new_scores[0][1],new_scores[0][2])
new_s = "?, ?, ?", (new_scores[2][0],new_scores[2][1],new_scores[2][2])
#update the database
scores.update(new_r, new_p, new_s, name)