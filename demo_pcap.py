import pandas as pd
df=pd.read_csv("/home/nabila/PycharmProjects/Team4/Network_project/nabila.csv")
print(df.columns)
print(df.groupby('Protocol').sum())