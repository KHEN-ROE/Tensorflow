import tensorflow as tf
from tensorflow.keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
#1
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("x_train.shape=", x_train.shape) # (60000, 28, 28)
print("y_train.shape=", y_train.shape) # (60000,)
print("x_test.shape=",  x_test.shape)  # (10000, 28, 28)
print("y_test.shape=",  y_test.shape)  # (10000,)

#2
nlabel, count = np.unique(y_train, return_counts=True)
print("nlabel:", nlabel)
print("count:",  count)
print("# of Class:",  len(nlabel) )

#3: display images
print("y_train[:8]=",y_train[:8])
fig = plt.figure(figsize=(8, 4))
for i in range(8):
    plt.subplot(2, 4, i + 1)  
    plt.imshow(x_train[i], cmap='gray')
    plt.axis("off")
fig.tight_layout()
plt.show()
