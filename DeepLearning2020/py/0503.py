# tf.keras.losses.MeanSquaredError() 사용하여 mse 계사
import numpy as np
import tensorflow as tf

t = np.array([1,   2, 3,   4])    
y1 = np.array([0.5, 1, 1.5, 2])
#t = tf.convert_to_tensor(t, dtype=tf.float32)
#y1 = tf.convert_to_tensor(y1, dtype=tf.float32)

MSE = tf.keras.losses.MeanSquaredError()

print("MSE(t, y1)=", MSE(t, y1).numpy())

y2 = np.array([0.5, 1.5, 2.5, 3.5])
print("MSE(t, y2)=", MSE(t, y2).numpy())
