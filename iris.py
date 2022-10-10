import pandas as pd

data = pd.read_csv("your downloaded dataset location ")

data.head()
data.sample(20)
data.columns
data.shape
print(data)
print(data[10:21])
sliced_data=data[10:21]
print(sliced_data)
specific_data=data[["Id","Species"]]
print(specific_data.head(10))
