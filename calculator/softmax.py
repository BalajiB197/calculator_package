# softmax.py
import numpy as np

def softmax(arg):
    '''returns the softmax of the input'''
    if len(arg) > 1:
        expo = np.exp(arg)
        expo_sum = np.sum(np.exp(arg))
        return expo/expo_sum
    else:
        return 'ERROR!!, more than one value is required'

def derivative_softmax(arg):
    '''returns the derivative of softmax of the input'''
    x = softmax(arg)
    s = x.reshape(-1,1)
    return (np.diagflat(s) - np.dot(s, s.T))