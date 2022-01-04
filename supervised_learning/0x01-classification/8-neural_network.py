#!/usr/bin/env python3
"""Simple neural network class"""


import numpy as np


class NeuralNetwork:
    """ Represnets simple neural network """

    def __init__(self, nx, nodes):
        """ Initialization method """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")
        self.W1 = np.ndarray((nodes, nx))
        self.W1 = np.random.normal(size=(nodes, nx))
        self.W2 = np.ndarray((1, nodes))
        self.W2[0] = np.random.normal(size=nodes)
        self.b1 = np.zeros((nodes, 1))
        self.b2 = 0
        self.A1 = 0
        self.A2 = 0