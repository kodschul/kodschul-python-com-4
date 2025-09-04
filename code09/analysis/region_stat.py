import pandas as pd 
import seaborn as sns 
import  matplotlib.pyplot as plt

df = pd.read_csv("umsatz_pro_ort.csv")

df_region = df.groupby(["RegionTyp"]).sum()


sns.barplot(x="RegionTyp", y="Umsatz", data=df_region)

plt.title("Umsatz je nach Region")
# plt.xlabel("Age")
# plt.ylabel("Gewicht")
plt.show()