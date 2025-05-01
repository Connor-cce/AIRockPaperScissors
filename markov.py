import numpy as np
import numpy.linalg as la
import random
import sqlite3

class predictor:
    def __init__(self, r, p, s):
        self.rock = self.stringToArray(r)
        self.paper = self.stringToArray(p)
        self.scissors = self.stringToArray(s)
        self.mark = np.array([self.rock, self.paper, self.scissors])
        self.last_Move = 0

    def stringToArray(self, valueString):
        tempArr = valueString.split(",")
        print(tempArr)
        for i in range(len(tempArr)):
            tempArr[i] = float(tempArr[i])
        return tempArr

    def add(self, origin, current):
        self.mark[origin][current] += 1.0

    def pick(self, array):
        self.maximum = max(array)
        self.returnList = []
        for i in range(3):
            if array[i] >= self.maximum:
                self.returnList.append(i)
        return random.choice(self.returnList)
    
    def decipherMove(self, str):
        if str == "rock":
            self.add(self.last_Move, 0)
            self.last_Move = 0
            return [1,0,0]
        elif str == "paper":
            self.add(self.last_Move, 1)
            self.last_Move = 1
            return [0,1,0]
        else:
            self.add(self.last_Move, 2)
            self.last_Move = 2
            return [0,0,1]
        
    def decipherMarkov(self, num):
        if num == 0:
            return "rock"
        elif num == 1:
            return "paper"
        else:
            return "scissors"

    def nextMove(self, move):
        self.A = self.mark.copy()
        for i in range(3):
            sum = np.sum(self.A[:,i])
            self.A[:,i] = (self.A[:,i]/sum)
        x = self.A @ self.decipherMove(move)
        print(self.mark)
        return self.decipherMarkov(self.pick(x))

    def getMark(self):
        return self.mark