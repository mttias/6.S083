# purpose: implement monte carlo engine testing financial managers w/ pure luck
# 10 000 managers w/ 50-50 chance of making $10 000

import random
import numpy as np

# init a financial manager
class Manager(object):
    def __init__(self, id, balance):
        self._id = id
        self._balance = balance
        self._alive = 1

    # gain 10k
    def addBalance(self):
        self._balance += 10000
    
    # if you lose balance: you die
    def remBalance(self):
        self._alive = 0
    
    # check if alive
    def isAlive(self):
        return self._alive

        # what is the balance
    def getBalance(self):
        return self._balance

# test = Manager(1, 0)
# print(test.getBalance())

# unfair die
def unfairDie():
    return random.randrange(100)

results = []
winners = []

# 10 000 bad managers battle it out til death (death = one bad year)
for i in range(50000):
    manager = Manager(i,0)
    print("init new manager")
    while manager.isAlive() == 1:
        val = unfairDie()
        if val < 45:
            manager.addBalance()
        elif val >= 45:
            manager.remBalance()
            results.append(manager.getBalance())
            exit
    
results.sort()

# prints winner
print(f"the winning bad manager ended at {results[-1]} USD after a {(results[-1]) / 10000} year streak")


