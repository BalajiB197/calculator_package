# relu.py
import numpy as np

def relu(arg):
   '''returns the relu value'''
   return np.maximum(0,arg)

def derivative_relu(arg):
    '''returns the derivative relu value'''
    arg = 1 if arg > 0 else 0
    return arg