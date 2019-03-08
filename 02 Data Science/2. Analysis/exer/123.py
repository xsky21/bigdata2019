import pandas as pd

data_frame = pd.read_csv("Zip_Stat.csv", index_col=None)
k = list(data_frame["COUNT PARTICIPANTS"].array)
k.sort()
print(k)
