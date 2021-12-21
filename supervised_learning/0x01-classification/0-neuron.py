#!/usr/bin/env python3
""" Module containing a Class of a neuron """
import numpy as np

class Neuron():
    """ Class representing a neuron """
    def __init__(self, nx) -> None:
        """ Initialization method """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.W = np.random.normal(size=(1,nx))
        self.b = 0
        self.A = 0
