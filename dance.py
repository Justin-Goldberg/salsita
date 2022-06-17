
import random

def salsa(measures):
        # learn a few moves
    steps = ['el huracan', 'patacon pisao', 'patineta', 'ciclon', 'basico']
        # get comfortable with your partner
    for measure in range(0, random.randint(1,5)):
        print(steps[-1])
        # time to boogie
    for measure in range(0, measures):
        print(steps[random.randint(0,4)])
