import pandas as pd 
import seaborn as sns 
import  matplotlib.pyplot as plt

df = pd.read_csv("umsatz_pro_ort.csv")

# df.groupby(["RegionTyp"]).sum().plot(kind="bar")
df.groupby(["RegionTyp"]).count().plot(kind="bar")


plt.title("Umsatz je nach Region")
# plt.xlabel("Age")
# plt.ylabel("Gewicht")
plt.show()