import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as am

#read the data set into a pandas DataFrame

wine = pd.read_csv('winequality-both.csv',sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

# display descriptive statistics for quality by wine type
print("<와인 종류에 따른 기술 통계를 출력하기>")
w = wine.groupby('type')
print(wine.groupby('type').describe())
