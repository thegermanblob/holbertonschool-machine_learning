#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

def calculate_loss(y, y_pred):
    """ Calculates the softmax cross-entropy loss """

    return tf.losses.softmax_cross_entropy(y, y_pred)