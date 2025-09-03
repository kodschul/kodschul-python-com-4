import pandas as pd 

df = pd.DataFrame({
    'Stadt': ["Berlin", "Berlin", "Hamburg", "Hamburg", "München"],
    'Bezirk': ['West', 'West', 'Ost', 'West', 'West'],
    'Umsatz': [100, 150, 200, 50, 300],
    # 'Bevölkerung': [1000, 1500, 2000, 500, 3000]
})

df_grouped = df.groupby(["Stadt", "Bezirk"]).sum()
print(df_grouped)

exit()

print(df)
df_agg_sum = df.groupby("Stadt").sum()


df_agg_mean = df.groupby("Stadt").mean()

df_agg = df.groupby("Stadt").agg({
    'Umsatz': ["sum", "mean", "count"],
    'Bevölkerung': ["sum", "mean", "count"],
})
print(df_agg)

