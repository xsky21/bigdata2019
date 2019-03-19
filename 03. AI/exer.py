import pandas as pd
from sklearn import svm, metrics

wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
k = pd.get_dummies(wine['type'], prefix='type2')
wine = wine.join(k)

data = wine.iloc[:,1:12]
data_type = wine.iloc[:,13]
data = data.join(data_type)
label = wine.iloc[:,12]

clf = svm.SVC(gamma='auto')
clf.fit(data, label)
pre = clf.predict(data)

#정답률 구하기
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer : ok += 1
    total += 1
print("정답률:", ok, "/", total, "=", ok/total)