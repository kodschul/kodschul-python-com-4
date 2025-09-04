import requests 
import pandas as pd

url = "https://rickandmortyapi.com/api/character"

response = requests.get(url) 
characters = response.json()["results"]

df = pd.DataFrame(characters)
df.to_csv("characters.csv", index=False)

print(len(df))