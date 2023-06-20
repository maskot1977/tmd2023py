import numpy as np

def qeq(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        return (( - b + np.sqrt(d)) / (2 * a), ( - b - np.sqrt(d)) / (2 * a))
    else:
        return (
            complex(- b/ (2 * a), np.sqrt(-d) / (2 * a)),
            complex(- b/ (2 * a), - np.sqrt(-d) / (2 * a))
        )
