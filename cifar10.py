import keras
import tensorflow as tf

from model import ELM
from keras.datasets import cifar10

# Basic tf setting
tf.set_random_seed(2016)
sess = tf.Session()

# Get data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

# Construct ELM
batch_size = 5000
hidden_num = 150
print("batch_size : {}".format(batch_size))
print("hidden_num : {}".format(hidden_num))
elm = ELM(sess, batch_size, 784, hidden_num, 10)

# one-step feed-forward training
train_x, train_y = mnist.train.next_batch(batch_size)
elm.feed(train_x, train_y)

# testing
elm.test(mnist.test.images, mnist.test.labels)
