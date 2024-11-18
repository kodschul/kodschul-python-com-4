import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("population.csv")

df.plot(kind="pie", x="country", y="population")
# small_df = df.head(10)
# small_df.plot(kind="bar", x="country", y="population")

plt.show()

# df.loc[0, 'population'] = 10
# for x in df.index:
#     if df.loc[x, 'population'] < 100:
#         df.drop(x, inplace=True)


# # -- Sort DataFrame
# df = pd.read_csv("population.csv")
# sorted_df = df.sort_values(by="population", ascending=False)
# top_5_df = sorted_df.head(5)

# top_5_countries = list(top_5_df['country'])

# print(f"Bevölkerung Top 5: {top_5_countries}")
