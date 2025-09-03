import pandas as pd 

customer_df = pd.DataFrame({
    'KundenID': [1,2,3],
    'Name': ["Anna", "Eva", "Mike"]
})

order_df = pd.DataFrame({
    'ProductID': [100, 200, 300],
    'KundenID': [2, 2, 1],
    'Betrag': [50, 70, 110]
})

print(customer_df)
print(order_df)

customer_order_df = pd.merge(customer_df, order_df, on="KundenID")
print(customer_order_df)