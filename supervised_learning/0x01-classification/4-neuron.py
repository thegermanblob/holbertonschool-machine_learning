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
        self.__W = np.random.normal(size=(1,nx))
        self.__b = 0
        self.__A = 0

    def forward_prop(self, X):
        """ Calculates the foward propagation """
        if type(X) is not np.ndarray:
            raise TypeError("X not array")
        z = -1 * (np.dot(self.__W, X) + self.__b)
        self.__A = 1/(1 + np.exp(z))
        return self.__A

    @property
    def W(self):
        """ Getter method for weights """
        return self.__W

    @property
    def b(self):
        """ Getter method for bias """
        return self.__b

    @property
    def A(self):
        """ Getter method for activated output """
        return self.__A

    def cost(self, Y, A):
        """ calculates cost of the model using logistic regression  """
        return -(Y * np.log(np.where(A== 0, 0.00000001, A)) + (1 - Y)* np.log(1.0000001 - A)).mean()


    def evaluate(self, X, Y):
        """ Evaluates the neurons prediction """
        prediction = self.forward_prop(X) 
        cost = self.cost(Y, prediction)
        return np.where(prediction >= 0.5, 1, 0), cost