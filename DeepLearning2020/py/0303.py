#텐서 생성
import tensorflow as tf
#1
a = tf.constant(1)
b = tf.constant([1, 2, 3, 4])
c = tf.constant([[1, 2], [3, 4]])
d = tf.constant([[[1, 2], [3, 4]]]) #shape을 이해해야 함. (1, 2, 2) 인데 왜? 대괄호 하나씩 걷어내면서 파악


#2
print(a)
print(a.dtype)
print(a.ndim, b.ndim, c.ndim, d.ndim)
print(a.shape, b.shape, c.shape, d.shape)

#3: indexing, slicing
print(b[0])
print(b[:2])
print(c[0, 0])
print(c[:,0])
