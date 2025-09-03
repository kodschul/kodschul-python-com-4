import pandas as pd

data = {
    'name': ["Marie", "Peter", ""],
    'age': [20, 15, 18]
}

df = pd.DataFrame(data)

print(df.describe())

df.to_csv("persons.csv", index=False)


# new_df = pd.read_csv("persons.csv")
# new_df.to_excel("person.xlsx", index=False)
