import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
# 데이터 출처 : 케글

# 수집 데이터 : csv형태의 파일
df = pd.read_csv("mushroom.csv", header=None)

# 데이터 요약 : 버섯의 모양, 색깔, 분포지역, 독성 여부에 대한 데이터를 담고 있는 데이터셋
# 고정변수 명시 : 독성 여부(e = 식용가능 , p = 독성)를 담고 있는 첫번째 열
# 독립변수 명시 : 첫번째 열을 제외한, 버섯의 특징을 담고 있는 나머지 열
# 각 필드의 의미
# 1열 독성 여부 2열 뚜껑 모양 3열 뚜껑 표면 4열 뚜껑 색깔 5열 흠집 유무
# 6열 냄새 종류 7열 뚜껑이 펴진 정도(우산처럼) 8열 뚜껑 안쪽에 있는 주름의 간격
# 9열 자실층 크기, 10열 자실층 색깔 11열 줄기 모양 12열 줄기-뿌리 13열 균환 윗부분의 줄기 표면
# 14열 균환 아랫부분의 줄기 표면 15열 균환 윗부분의 색깔 16열 균환 아랫부분의 색깔
# 17열 포피막 종류 18열 포피막 색깔 19열 균환 숫자 20열 균환 종류 21열 포자 색깔
# 22열 분포 23열 생장지

# 변수설정. X 독립변수 Y 종속변수
X = tf.placeholder(tf.float32, [None,22])
Y = tf.placeholder(tf.float32, [None,2])

label = []
data = []

label_p = [0,0]
label_e = [1,1]

for row_index, row in df.iterrows():
    if row.loc[0] == 'p':
        label.append(label_p)
    else :
        label.append(label_e)
    row_data = []
    for v in row.loc[1:]:
        row_data.append(ord(v))
    data.append(row_data)

W = tf.Variable(tf.zeros([22,2])) # 독립변수가 22개, 종속변수는 값이 2개
b = tf.Variable(tf.zeros([2]))

logit_y = tf.matmul(X,W) + b

#활성화 함수 설정 : 소프트맥스
softmax_y = tf.nn.softmax(logit_y)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y),reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

data_train, data_test, label_train, label_test = train_test_split(data, label)

# 손실함수 및 학습
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000) :
    sess.run(train_step, feed_dict={X:data_train, Y:label_train})

# 결과 예측
correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))

#결과 검증
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict={X: data_test, Y: label_test}))

#정확도 100%



