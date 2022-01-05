#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

def create_placeholders(nx, clases):
    """ creates and returns place holders for data """
    x = tf.placeholder("float", shape=(None,nx), name="x")
    y = tf.placeholder("float", shape=(None,clases), name="y")
    return x, y