import random
import numpy as np
# purpose: check pascal's 24-roll dice calculations

def roll_die():
    return random.choice([1,2,3,4,5,6])

# here we move beyond abstract discrete mathematics
# to a brute-force trial and errors
def check_pascal(num_trials):
    num_wins = 0
    for i in range(num_trials):
        for j in range(24):
            # roll dice 1 & 2 (return an int 1-6)
            d1 = roll_die()
            d2 = roll_die()
            if d1 == 6 and d2 == 6:
                num_wins += 1
                break
    print(f"odds off success are {num_wins / num_trials}")

check_pascal(1000000)