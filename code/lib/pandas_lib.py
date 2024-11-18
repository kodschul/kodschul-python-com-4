import pandas as pd
import numpy as np

df = pd.read_csv("population.csv", encoding="utf-8")


# sort countries by population ascending, top populated countries
# top_countries_by_pop_df = df.sort_values(by="population", ascending=False)
# print(top_countries_by_pop_df.head(10))

# calculate median
population = df['Land Area (Km²)']
print(population.describe())
exit()


# calculate the total rows
total_countries = len(df)
print(f"Total countries: {total_countries}")


# calculate the  average population
population = df['population']
np_population = np.array(population)
avg_population = round(np_population.mean() / 1e6, 2)
print(f"Out of {total_countries} Countries there is an average population of: {avg_population} million")
