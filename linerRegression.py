import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn.linear_model as LinearRegression

data_set="https://github.com/ageron/data/raw/main/lifesat/lifesat.csv"
data=pd.read_csv(data_set)
data_cp=data[["GDP per capita (USD)"]].values
data_st=data[["Life satisfaction"]].values
model = LinearRegression.LinearRegression()
model.fit(data_cp,data_st)
print(model.score(data_cp,data_st))
plt.scatter(data_cp,data_st)
plt.xlabel("GDP per capita (USD)")
plt.ylabel("Life satisfaction")
plt.title("GDP per capita vs Life satisfaction")
# plt.legend()
# plt.grid()
plt.show()

# print(model.predict([[50000]]))