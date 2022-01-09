#!/usr/bin/env python3
import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer
tf.disable_eager_execution()

def forward_prop(x, layer_sizes=[], activations=[]):
    """
    creates the forward propagation graph for the neural network 

    x is the placeholder for the input data
    layer_sizes is a list containing the number of nodes in each layer of the network
    activations is a list containing the activation functions for each layer of the network
    Returns: the prediction of the network in tensor form

    """
    if len(activations) == 1:
        a = activations[0]
    else:
        a = None

    for i, n in enumerate(layer_sizes):
        if a is not None:
            fp = create_layer(x, n, a)
        else:
            fp = create_layer(x, n, activations[i])
    return fp
