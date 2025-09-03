import pandas as pd 

customer_df = pd.DataFrame({
    'KundenID': [1,2,3],
    'Name': ["Anna", "Eva", "Mike"]
})

order_df = pd.DataFrame({
    'BestellID': [100, 200, 300, 400],
    'KundenID': [2, 2, 1, -1000],
    'Betrag': [50, 70, 110, 220]
})

print(customer_df)
print(order_df)

customer_order_df = pd.merge(customer_df, order_df, on="KundenID", how="left")
print(customer_order_df)

# left join

# customer_order_df = pd.merge(customer_df, order_df, on="KundenID", how="left")
# print(customer_order_df)