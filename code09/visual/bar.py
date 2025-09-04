import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("../io/data/Deutschland_Cities.csv")



x = [1,2,3]

x_square = [x**2 for x in x]


df["city"] = [ x[0:3] for x in df["city"]]


df.sort_values(by="population", ascending=False)



# plt.figure(figsize=(12, 5))

sns.barplot(x="city", y="population", data=df.head(10))

plt.title("Bevölkerung Deutschland")
plt.xlabel("Stadt")
plt.ylabel("Bevölkerung")
plt.show()
