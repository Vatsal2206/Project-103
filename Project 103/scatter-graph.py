import pandas as pd
import plotly.express as pe

df = pd.read_csv('Copy+of+data+-+data.csv')
scatterGraph = pe.scatter(df, x='date', y = 'cases', color='country')
scatterGraph.show()