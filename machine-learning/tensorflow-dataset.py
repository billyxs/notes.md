# https://towardsdatascience.com/how-to-use-dataset-in-tensorflow-c758ef9e442 8

import numpy as np
import tensorflow as tf

x = np.random.sample((100, 2))
dataset = tf.data.Dataset.from_tensor_slices(x)
