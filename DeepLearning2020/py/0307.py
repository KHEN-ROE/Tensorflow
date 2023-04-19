# reshapre 사용법
import tensorflow as tf
#1
a = tf.range(6)
#print(a)

b = tf.reshape(a, shape=(2, 3)) 
#b = tf.reshape(a, shape=(-1, 3)) - 1해도 결과 같네

print(b)

c = tf.reshape(b, shape=(-1,))
#print(c)

#2
d = tf.transpose(b) # tf.transpose(b, perm=[1, 0])
#print(d)
