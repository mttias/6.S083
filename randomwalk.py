# a random walk using the secrets module
import secrets

steps = 0
endstate = []

for y in range(100):
    steps = 0
    for x in range (10000):
        if float(secrets.randbelow(2)) == 0:
            steps += 1
            # print(steps, "+1")
        else:
            steps -= 1
            # print(steps, "-1")
    endstate.append(steps)

print(endstate)
# what if we do lots of simulations of this and see where we end up?
# matplotlib x-y axis dot diagram