# sigmoid.py
import numpy as np

def sigmoid(arg):
   '''Return the sigmoid value'''
   if len(arg) > 1:
      return 1/(1+np.exp(-arg))
   else:
      return 'ERROR!!, more than one value is required'

def derivative_sigmoid(arg):
   '''Return the derivative of sigmoid value'''
   return sigmoid(arg) * (1 - sigmoid(arg))

# reference 
# https://stackoverflow.com/questions/49977063/role-derivative-of-sigmoid-function-in-neural-networks