#https://www.sohamkamani.com/blog/2018/01/07/tensorflow-introduction/

import tensorflow as tf


print(tf.VERSION)

a = tf.constant(3.0)
b = tf.constant(2.0)

c = a+b

sess = tf.Session()

print(sess.run(c))

d = tf.placeholder(tf.float32)
e = tf.placeholder(tf.float32)

f = d+e

sess2 = tf.Session()

print(sess2.run(f, {d: 1, e: 5}))

g = tf.placeholder(tf.float32, shape=(2,1))
h = tf.placeholder(tf.float32, shape=(1,2))

i = tf.matmul(g, h)

sess3 = tf.Session()

print(sess3.run(i, {g: [[1],[2]], h: [[3, 4]]}))
