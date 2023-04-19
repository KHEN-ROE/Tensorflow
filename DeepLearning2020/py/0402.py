import tensorflow as tf
#1
a = tf.reshape(tf.range(12), shape = (3, 4))
print(a)

#2 
print(tf.reduce_min(a))
print(tf.reduce_min(a, axis= 0))
print(tf.reduce_min(a, axis= 1))

#3
print(tf.reduce_max(a))
print(tf.reduce_max(a, axis= 0))
print(tf.reduce_max(a, axis= 1))

#4
print(tf.reduce_sum(a))
print(tf.reduce_sum(a, axis= 0))
print(tf.reduce_sum(a, axis= 1))

#5 - 경사 하강법에서 사용
print(tf.reduce_mean(a))
print(tf.reduce_mean(a, axis= 0))
print(tf.reduce_mean(a, axis= 1))

#6
print(tf.reduce_prod(a))
print(tf.reduce_prod(a, axis= 0))
print(tf.reduce_prod(a, axis= 1))

#7 - 학습 시에 셔플 사용
a = tf.reshape(tf.random.shuffle(tf.range(12)), shape = (3, 4))
print(a)
# 학습 시에 사용 argmin() - 최소값을 갖는 값의 인덱스 argmax()는 그 반대
print(tf.argmin(a)) #  tf.argmin(a, axis =0)
print(tf.argmin(a, axis =1))
print(tf.argmax(a)) # tf.argmax(a, axis =0)
print(tf.argmax(a, axis =1))

#8 - 훈련 데이터 학습에 사용
a = tf.random.shuffle(tf.range(12))
print(a)
print(tf.sort(a)) # direction="ASCENDING"
print(tf.sort(a, direction="DESCENDING"))

# 전처리에 사용
a = tf.reshape(a, shape=(3, 4))
print(a)
print(tf.sort(a)) # tf.sort(a, axis = 1)
print(tf.sort(a, axis = 0))
