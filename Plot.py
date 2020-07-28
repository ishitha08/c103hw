import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.line(df, x="Date", y="No. of cases", color="Country", title='Corona cases in the world')

fig.show()
