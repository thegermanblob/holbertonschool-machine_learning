#!/usr/bin/env python3
import tensorflow.compat.v1 as tf
tf.disable_eager_execution()


def create_layer(prev, n, activation):
    """ Creates a layer for the network """
    init = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=init, name="layer")
    return layer(prev)
