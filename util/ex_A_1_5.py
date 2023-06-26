import numpy as np

def throw_dice(n):
    return sum(np.random.randint(6, size=(n)) + 1)
