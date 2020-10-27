# softmax.py
import numpy as np

def softmax(arg):
    expo = np.exp(arg)
    expo_sum = np.sum(np.exp(arg))
    return expo/expo_sum