# 텐서의 rank, type, share를 이해해야 함
import tensorflow as tf
#1
a = tf.Variable(1)
b = tf.Variable([1, 2, 3, 4])
c = tf.Variable([[1, 2], [3, 4]])
d = tf.Variable([[[1, 2], [3, 4]]])
print(a.dtype)
print(a.shape, b.shape, c.shape, d.shape)
 
#2
print(a)
print(a.read_value()) # a.value()
print(a.trainable)

#3: indexing, slicing - 데이터셋에서 훈련데이터, 검증데이터 추출
print(b[0])
print(b[:2])
print(c[0, 0])
print(c[:,0])

#4: assign(), assign_add(), assign_sub() - 학습한 후에 가중치 변경
print(id(a))
print(a.assign(10)) # a.assign(20, read_value=False) : no return
print(a.assign_add(20))
print(a.assign_sub(10))
print(id(a))
