import pandas as pd

churn = pd.read_csv('churn.csv', sep=',', header=0)

k = churn['Phone']
t = k.array
pass