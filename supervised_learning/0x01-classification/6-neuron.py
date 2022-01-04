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
        self.__W = np.random.normal(size=(1, nx))
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
        return -(Y * np.log(np.where(A == 0, 0.00000001, A)) + (1 - Y) * np.log(1.0000001 - A)).mean()

    def evaluate(self, X, Y):
        """ Evaluates the neurons prediction """
        prediction = self.forward_prop(X)
        cost = self.cost(Y, prediction)
        return np.where(prediction >= 0.5, 1, 0), cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """ Calculates one pass of gradient descent on the neuron 
            Args:
                X (np.ndarray): input data
                Y (np.ndarray): correct labels for the input data
                A (np.ndarray): activated output of the neuron with
                shape (1, m) where m is the number of examples
                alpha (float): learning rate.
        """  # ?
        m = len(Y[0])
        grad = np.matmul(X, (A - Y).T) / m
        self.__W -= alpha * grad.T
        # Whats right gets a lower bias on
        self.__b -= alpha * np.average(A - Y)

    def train(self, X, Y, iterations=5000, alpha=0.05):
        """ Trains the neuron """
