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

# fair die 50-50
def roll_die():
    return random.choice([1,2])

results = []

for i in range(10000):
    manager = Manager(i,0)
    print("init new manager")
    while manager.isAlive() == 1:
        val = roll_die()
        print("rolled die")
        if val == 1:
            manager.addBalance()
            print("added balance")
        elif val == 2:
            manager.remBalance()
            results.append(manager.getBalance())
            print("manager died")
            exit
    
results.sort()
print(results)


