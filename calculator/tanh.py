# tanh.py
import math

def tanh(arg):
    '''Return the value of tanh'''
    return math.tanh(arg)

def derivative_tanh(arg):
    '''Return the derivative value of tanh'''
    return 1-(math.tanh(arg))**2