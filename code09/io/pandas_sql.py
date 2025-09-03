import pandas as pd
from sql_db import conn


df = pd.read_sql("SELECT * FROM customers", con=conn)
print(df)
