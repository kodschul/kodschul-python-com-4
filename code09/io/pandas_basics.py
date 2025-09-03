import pandas as pd 

# Create DF
shopping_items = [
    {'name': 'orange', 'qty': 7, 'unit_price': 0.99},
    {'name': 'mango', 'qty': 6, 'unit_price': 2.99},
    {'name': 'lemonade', 'qty': 5, 'unit_price': 1.99},
]

shopping_df = pd.DataFrame(shopping_items)

shopping_df.to_csv("data/shopping_items.csv",  index_label="id")
shopping_df.to_excel("data/shopping_items.xlsx", index_label="id")
# shopping_df.to_json("data/shopping_items.json")
# shopping_df.to_html("data/shopping_items.html")

# Read Excel file
df = pd.read_excel("data/shopping_items.xlsx")
print(df)
exit()


# Read csv file
df = pd.read_csv("data/products.csv")

df['brutto_preis'] = df['price'] * 1.19

# (INCLUDE)
df1 = df[ df["price"] == 10 ]

# NOT INCLUDE 
df2 = df[~ (df["age"] == 10) ]

# COMBINED (=x or  y=y)
df2 = df[ (df["age"] != 10) & (df["age"] != 15)]

print(df1, df2)