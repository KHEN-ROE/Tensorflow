# stack, concat
import tensorflow as tf

#1
a = tf.constant([1, 2])  # [1, 2]
b = tf.constant([3, 4])  # [3, 4]

#2
#print(tf.stack([a, b])) # axis = 0 #0 이면 열기준, 1이면 행 기준
#print(tf.stack([a, b], axis = 1))
 
#3
print(tf.concat([a, b],axis =0))
a = tf.reshape(a, shape=(1,2))
b = tf.reshape(b, shape=(1,2))
c = tf.concat([a, b],axis =0)
#print(c)
 
#print(tf.concat([a, b],axis =1))
#print(tf.concat([c, b],axis =0))

b = tf.reshape(b, shape=(2,1))
#print(b)

#print(tf.concat([c, b],axis =1))
