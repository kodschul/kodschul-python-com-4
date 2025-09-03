import pandas as pd 

df = pd.read_csv("data/inventory.csv")
print(df.head(2))
print(df.tail(2))


df = pd.read_csv("data/products.csv")

df = df[[  'qty','price',]]

print(df.columns)
print(df)
exit()

# by index + column name
orange_price1  = df.loc[1, "price"]

# by index + column index
orange_price2  = df.iloc[1, 1]
print(orange_price1, orange_price2)






#### FILTER
# df1 = df[ df["name"].str.contains("e") ]
# print(df1)

### SORT 
sorted_df = df.sort_values(by=["price"], ascending=True)

print(sorted_df)