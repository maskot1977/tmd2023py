import numpy as np

def qeq(a, b, c):
  d = b ** 2 - 4 * a * c
  return (( - b + np.sqrt(d)) / (2 * a), ( - b - np.sqrt(d)) / (2 * a))
