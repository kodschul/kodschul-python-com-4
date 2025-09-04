import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


# df = pd.read_csv("data/people_stats.csv")


df = pd.DataFrame({
    'Alter': [10, 20, 30, 40, 50],
    'Einkommen': [0, 1000, 2000, 5000, 10000],
    'Score': [100, 4, 5, 3, 10]
})

df_numerical = df[["Alter", "Einkommen", "Score"]]


correlation = df_numerical.corr()


sns.scatterplot(x="Alter", y="Einkommen",data=df_numerical)
#sns.heatmap(correlation, annot=True, cmap="coolwarm")


plt.title("Korrelation")
plt.show()
