import tensorflow as tf

# .반드시 (()) 로 인자를 사용해야 한다.
ta = tf.zeros((2,2)) # ta는 {Tensor}

# print(ta.eval()) # 에러 발생

session = tf.InteractiveSession() # session은 {InteractiveSession}
print(ta.eval())
session.close()
