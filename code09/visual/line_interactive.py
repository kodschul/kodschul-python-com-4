import plotly.express as px 
import plotly.io as pio
import pandas as pd 

pio.renderers.default = "browser"


df = pd.DataFrame({
    'Alter': [10, 20, 30, 40, 50],
    'Einkommen': [0, 1000, 2000, 5000, 10000],
    'Score': [100, 4, 5, 3, 10]
})


fig = px.line(df, x="Alter", y="Einkommen", title="Alter vs Einkommen")
fig.show()
