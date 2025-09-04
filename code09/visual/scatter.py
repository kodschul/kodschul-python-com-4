import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("data/people_stats.csv")


# df.sort_values(by="population", ascending=False)

# sns.scatterplot(x="Height", y="Weight", data=df)

# plt.title("Größe vs Gewicht")
# plt.xlabel("Größe")
# plt.ylabel("Gewicht")
# plt.show()


sns.scatterplot(x="Age", y="Weight", hue="Gender", data=df)

plt.title("Age vs Gewicht")
plt.xlabel("Age")
plt.ylabel("Gewicht")
plt.show()
