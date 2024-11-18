import pandas as pd

# fruits = ["orange", "mango", "apple", "lemonade"]

fruits = [
    {'name': 'orange', 'price': 10},
    {'name': 'mango', 'price': 20},
    {'name': 'apple', 'price': 10},
    {'name': 'apple', 'price': 5}
]

df = pd.DataFrame(fruits)


# head_df = df.head(2)
name_column = df['name']

# new_df = df.drop_duplicates('name')
sorted_df = df.sort_values(by='price', ascending=False)


sorted_df.to_csv("fruits.csv", index=False)
