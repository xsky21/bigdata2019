import pandas as pd

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',',header=0)
k = wine['volatile acidity','citric acid']
