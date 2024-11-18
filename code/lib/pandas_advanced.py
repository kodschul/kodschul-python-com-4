import pandas as pd

df = pd.read_csv("people.csv")

filtered_df = df[(df['age'] > 0) & (df['age'] < 120)]
filtered_df = filtered_df[(df['weight'] > 0) & (df['weight'] < 500)]

print(filtered_df)
print(f"Avg age: {filtered_df['age'].mean()}")

print(df)
