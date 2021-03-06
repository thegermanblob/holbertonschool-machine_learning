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

    @property
    def b1(self):
        return self.__b1

    @property
    def b2(self):
        return self.__b2
    @property
    def W1(self):
        return self.__W1

    @property
    def W2(self):
        return self.__W2

    @property
    def A1(self):
        return self.__A1

    @property
    def A2(self):
        return self.__A2

    def forward_prop(self, X):
        """ Calculate forward propagation of neural network """
        self.__A1 = np.dot(self.__W1, X) + self.__b1
        self.__A1 = 1 / (1 + np.exp(-1 * self.__A1))
        self.__A2 = (np.dot(self.__W2, self.__A1) +
                     self.__b2)
        self.__A2 = 1 / (1 + np.exp(-1 * self.__A2))
        return self.__A1, self.__A2
    
    def cost(self, Y, A):
        """ Calculate cost of the neural network """
        return -(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)).mean()

    def evaluate(self, X, Y):
        """ Evaluates neural network """
        return (self.forward_prop(X)[1].round().astype(int),
                self.cost(Y, self._A2))

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """ Performs a step of gradient descent on the neural network  """
        d2 = A2 - Y
        d1 = np.dot(self.__W2.T, d2) * A1 * (1 - A1)
        self.__W2 -= alpha * np.dot(d2, A1.T) / A1.shape[1]
        self.__b2 -= alpha * d2.mean(axis=1, keepdims=True)
        self.__W1 -= alpha * np.dot(d1, X.T) / X.shape[1]
        self.__b1 -= alpha * d1.mean(axis=1, keepdims=True)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """ Trains the network """
        if type(iterations) is not int:
            raise TypeError("iterations must be an integer")
        if iterations <= 0:
            raise ValueError("iterations must be a positive integer")
        if type(alpha) is not float:
            raise TypeError("alpha must be a float")
        if alpha <= 0:
            raise ValueError("alpha must be positive")
        while iterations > 0:
            self.gradient_descent(X, Y, *self.forward_prop(X), alpha)
            iterations -= 1
        return self.evaluate(X, Y)

    