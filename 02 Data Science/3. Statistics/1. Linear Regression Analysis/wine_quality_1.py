import pandas as pd

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',',header=0)
#wine.columns = wine.columns.str.replace(' ', '_')
#print(wine.head())

print(wine.index)
#print("변수별 요약통계 표시")
#print(wine.describe())
pass
#print("\n유일값 찾기")
#print(sorted(wine.quality.unique()))

#print("\n빈도 찾기")
#print(wine.quality.value_counts())