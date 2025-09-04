import seaborn as sns
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv("data/people_stats.csv")



sns.histplot(df['Weight'], bins=10, kde=True)

plt.title("Gewichtverteilung")

plt.show()
