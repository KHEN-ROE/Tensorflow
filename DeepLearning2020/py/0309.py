# 데이터 전처리에 차원 확장
import tensorflow as tf
#1
a = tf.constant([1, 2])
#print(a)

b = tf.expand_dims(a, axis = 0) # 행으로 차원 확장?
#print(b)

c = tf.expand_dims(a, axis = 1) # 열로 차원 확장?
print(c)

d = tf.expand_dims(c, axis = 0)
#print(d)

#2
e = tf.squeeze(d) # remove all axes of shape size = 1
#print(e)

f = tf.squeeze(d, axis = 2)
#print(f)
