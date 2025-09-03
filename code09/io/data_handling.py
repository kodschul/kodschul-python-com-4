import pandas as pd 


df = pd.read_csv("data/Deutschland_Cities.csv")

df.dropna()
df['population'].fillna(0, inplace=True)

# clean_df = df.dropna(subset=["population"])


# print(len(df), len(clean_df))

# print(df.isna().sum())

print(df)