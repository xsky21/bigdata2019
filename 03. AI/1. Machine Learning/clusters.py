import pandas as pd
import sklearn.cluster, sklearn.preprocessing
from sklearn import metrics

alco2009 = pd.read_csv("niaaa-report2009.csv",index_col="State")
columns = ["wine","Beer"]
# 클러스터링 객체를 생성하고 모델을 학습시킨다.
kmeans = sklearn.cluster.KMeans(n_clusters=9)
kmeans.fit(alco2009[columns])
alco2009["Clusters"] = kmeans.labes_

alco2009.to_csv("Clustering_Result.csv", index=False)

data = alco2009[["Wine","Beer"]]
label = alco2009["Clusters"]

predicted_result = kmeans.predict(data)
print("예측 클러스터링 결과")
print(predicted_result)
print("정답률: %s %%"%(metrics.accurace_score(label, predicted_result)*100))