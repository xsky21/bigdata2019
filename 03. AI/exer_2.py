import pandas as pd
from sklearn import svm, metrics

house = pd.read_csv('Housing.csv', sep=',', header=0)
k = pd.get_dummies(house.iloc[:,[6,7,8,9,10,12]])
house = house.join(k.iloc[:,[0,2,4,6,8,10]])
data = house.iloc[:,[2,3,4,5,11,13,14,15,16,17,18]]
label = house.iloc[:,1]

clf = svm.SVC(gamma='auto')
clf.fit(data, label)
pre = clf.predict(data)

#정답률 구하
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer : ok += 1
    total += 1
print("정답률:", ok, "/", total, "=", ok/total)