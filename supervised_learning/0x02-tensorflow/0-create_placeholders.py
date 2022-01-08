#!/usr/bin/env python3

import tensorflow.compat.v1 as tf
tf.disable_eager_execution()

def create_placeholders(nx, classes):
    """ creates and returns place holders for data """
    x = tf.placeholder("float", shape=[None,nx], name="x")
    y = tf.placeholder("float", shape=[None,classes], name="y")
    return x, y