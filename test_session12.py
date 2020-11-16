import os
import pytest
import calculator
from calculator import derivative
from math import cos, exp, log, sin, tan, tanh
import numpy as np

mmatrix= np.array([[1,2,3],[4,5,6]])
mmatrix_single = np.array([[1]])

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_file_for_formatting():
    '''Checks for Readme File formatting'''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 1
    
def test_cos():
    assert calculator.cos(4) == cos(4)

def test_exp():
    assert calculator.e(4) == exp(4)

def test_relu():
    assert calculator.relu(4) == np.maximum(0,4)

def test_sigmoid():
    print(calculator.sigmoid(mmatrix))

def test_softmax():
    print(calculator.softmax(mmatrix))

def test_sigmoid_len():
    assert calculator.sigmoid(mmatrix_single) == 'ERROR!!, more than one value is required'

def test_softmax_len():
     assert calculator.softmax(mmatrix_single) == 'ERROR!!, more than one value is required'

def test_sin():
    assert calculator.sin(4) == sin(4)

def test_tan():
    assert calculator.tan(4) == tan(4)

def test_tanh():
    assert calculator.tanh(4) == tanh(4)

def test_derivative_exp():
    assert derivative.derivative_e(1) == exp(1)

def test_derivative_log():
    assert derivative.derivative_log(2) == 1/2

def test_derivative_tanh():
    assert derivative.derivative_tanh(90) ==  1-(tanh(90))**2

def test_derivative_tan():
    assert derivative.derivative_tan(90) == (1/cos(90))**2

def test_derivative_cos():
    assert derivative.derivative_cos(90) == -calculator.sin(90)