import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as am

#read the data set into a pandas DataFrame

wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

# display descriptive statistics for quality by wine type
print("<와인 종류에 따른 기술 통계를 출력하기>")
print(wine.groupby('type')['alcohol'].describe().unstack())

# Calculate specific quantiles
print("<특정 사분위수 계산하기 >")
print(wine.groupby('type')['quality'].quantile([0.25, 0.75]))

print("\n"+'='*80)
print("7.2.2 그룹화, 히스토그램, t 검정")
red_wine = wine.loc[wine['type']=='red','quality']
print(red_wine)
white_wine = wine.loc[wine['type']=='white','quality']
