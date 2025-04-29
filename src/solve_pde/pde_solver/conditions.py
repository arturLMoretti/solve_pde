import numpy as np

def initial_condition_sin(x):
    return np.sin(np.pi * x)

def initial_condition_gaussian(x, center=0.5, width=0.1):
    return np.exp(-((x - center) ** 2) / (2 * width ** 2))
