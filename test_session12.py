import os
import pytest
import calculator
from math import cos, exp, log, sin, tan, tanh
import numpy as np

mmatrix= np.array([[1,2,3],[4,5,6]])

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_cos():
    assert calculator.cos(4) == f'{cos(4)}'

def test_exp():
    assert calculator.e(4) == f'{exp(4)}'

def test_relu():
    assert calculator.relu(4) == f'{np.maximum(0,4)}'

def test_sigmoid():
    print(f'{calculator.sigmoid(mmatrix)}')

def test_sin():
    assert calculator.sin(4) == f'{sin(4)}'

def test_softmax():
    print(f'{calculator.softmax(mmatrix)}')

def test_tan():
    assert calculator.tan(4) == f'{tan(4)}'

def test_tanh():
    assert calculator.tanh(4) == f'{tanh(4)}'