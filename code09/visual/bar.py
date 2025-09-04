import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("../io/data/Deutschland_Cities.csv")


df.sort_values(by="population", ascending=False)

sns.barplot(x="city", y="population", data=df.head(10))

plt.title("Bevölkerung Deutschland")
plt.xlabel("Stadt")
plt.ylabel("Bevölkerung")
plt.show()
