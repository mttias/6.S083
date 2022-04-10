import random
import numpy as np

def unfairDie():
    return random.randrange(100)

for x in range(100):
    print(unfairDie())