import pandas as pd

import plotly_express as px

df=pd.read_csv("line_chart.csv")

fig=px.bar(df,x="Year",y="Per capita income",color="Country",title="Per Capita Income")

fig.show()