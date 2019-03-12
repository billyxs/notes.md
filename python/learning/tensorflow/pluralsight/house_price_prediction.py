# house_price_prediction
#
#  This is a very simple prediction of house prices based on house size
#  implemented in Tensorflow

import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# generation of some house sizes between 1000 and 3500 sq ft
num_house = 160
np.random.seed(42)
house_size = np.random.randint(low=1000, high=3500, size=num_house)

# generate house prices from house size with a random number added
np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(
    low=20000, high=70000, size=num_house
)

# plot generated house and size
plt.plot(house_size, house_price, "bx")  # bx = blue x
plt.ylabel("Price")
plt.xlabel("Size")
plt.show()


def normalize(array):
    """ need to normalize values to prevent under/overflows."""
    return (array - array.mean()) / array.std()


# define number of training samples, 0.7 = 70%. We can take the first
# 70% since the values are randomized
num_train_samples = math.floor(num_house * 0.7)

# define training data
train_house_size = np.asarray(house_size[:num_train_samples])
train_price = np.asanyarray(house_price[:num_train_samples:])

train_house_size_norm = normalize(train_house_size)
train_price_norm = normalize(train_price)

# define test data
test_house_size = np.array(house_size[num_train_samples:])
test_house_price = np.array(house_price[num_train_samples:])

test_house_size_norm = normalize(test_house_size)
test_house_price_norm = normalize(test_house_price)


# set up the tensorflow  placeholders that get updated as we descend down the
# gradient
tf_house_size = tf.placeholder("float", name="house_size")
tf_price = tf.placeholder("float", name="price")

# define the variables holding the size_factor and price we set during training
# we initialize them to some random values based on the normal distribution
tf_size_factor = tf.Variable(np.random.randn(), name="size_factor")
tf_price_offset = tf.Variable(np.random.randn(), name="price_offset")

# define the
tf_price_pred = tf.add(tf.multiply(
    tf_size_factor, tf_house_size), tf_price_offset
)

# 3. define the Loss Function (how much error) - Mean squared error
tf_cost = tf.reduce_sum(
    tf.pow(tf_price_pred-tf_price, 2)
)/(2*num_train_samples)

# Optimizer learning rate. The size of the steps down the gradient
learning_rate = 0.1

# 4. define a Gradient descent optimizer that will minimize the loss
# defined in the operation "cost".
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(tf_cost)

# initialize the variables
init = tf.global_variables_initializer()


# tf.Session()
# tf.run()
# tf.close()
with tf.Session() as sess:
    sess.run(init)

    # set how often to display training progress and number of training
    # iterations
    display_every = 2
    num_training_tier = 50

    # keep iterating the training data
    for iteration in range(num_training_tier):

        # fit all training data
        for (x, y) in zip(train_house_size_norm, train_price_norm):
            sess.run(optimizer, feed_dict={tf_house_size: x, tf_price: y})

        # display current status
        if (iteration + 1) % display_every == 0:
            c = sess.run(tf_cost, feed_dict={
                tf_house_size: train_house_size_norm,
                tf_price: train_price_norm
            })
            print("iteration #:", '%04d' % (iteration + 1),
                  "cost=", "{:.9f}".format(c), "size_factor=",
                  sess.run(tf_size_factor), "price_offset=",
                  sess.run(tf_price_offset))

    print("Optimization finished!")
    training_cost = sess.run(tf_cost, feed_dict={
        tf_house_size: train_house_size_norm,
        tf_price: train_price_norm
    })
    print("Trained cost=", training_cost, "size_factor=",
          sess.run(tf_size_factor), "price_offset=",
          sess.run(tf_price_offset), '\n')

    train_house_size_std = train_house_size.std()
    train_house_size_mean = train_house_size.mean()
    train_price_mean = train_price.mean()
    train_price_std = train_price.std()

    # plot the graph
    plt.rcParams["figure.figsize"] = (10, 8)
    plt.figure()
    plt.ylabel("price")
    plt.xlabel("Size (sq.ft)")
    plt.plot(train_house_size, train_price, 'go', label='Training data')
    plt.plot(test_house_size, test_house_price, 'mo', label='Testing data')
    plt.plot(train_house_size_norm * train_house_size_std +
             train_house_size_mean, (sess.run(tf_size_factor) *
                train_house_size_norm + sess.run(tf_price_offset)) *
             train_price_std + train_price_mean, label="Learned Regression")

    plt.legend(loc="upper left")
    plt.show()

