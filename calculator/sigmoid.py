# sigmoid.py
import numpy as np

def sigmoid(arg):
   return f'{1/(1+np.exp(-arg))}'