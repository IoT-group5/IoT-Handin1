import pandas as pd
import glob
import plotly.express as px
import plotly.graph_objects as go

df1 = pd.read_csv('csv/siggenroom1rhum.csv')
df2 = pd.read_csv('csv/siggenroom1temp.csv')
df3 = pd.read_csv('csv/siggenroom2rhum.csv')
df4 = pd.read_csv('csv/siggenroom2temp.csv')

df5 = pd.read_csv('csv/mavgroom1rhumrec.csv')
df6 = pd.read_csv('csv/mavgroom1temprec.csv')
df7 = pd.read_csv('csv/mavgroom1temppub.csv')
df8 = pd.read_csv('csv/mavgroom1rhumpub.csv')
df9 = pd.read_csv('csv/mavgroom2temprec.csv')
df10 = pd.read_csv('csv/mavgroom2rhumrec.csv')
df11 = pd.read_csv('csv/mavgroom2temppub.csv')
df12 = pd.read_csv('csv/mavgroom2rhumpub.csv')

df13 = pd.read_csv('csv/funcroom1temp.csv')
df14 = pd.read_csv('csv/funcroom1rhum.csv')
df15 = pd.read_csv('csv/funcroom2temp.csv')
df16 = pd.read_csv('csv/funcroom2rhum.csv')
df17 = pd.read_csv('csv/funcroom1ahum.csv')
df18 = pd.read_csv('csv/funcroom2ahum.csv')

trace1 = go.Line(x=df1["timestamp"], y=df1["value"], name="siggenroom1rhum", line=dict(width=5))
trace2 = go.Line(x=df2["timestamp"], y=df2["value"], name="siggenroom1temp", line=dict(width=5))
trace3 = go.Line(x=df3["timestamp"], y=df3["value"], name="siggenroom2rhum", line=dict(width=5))
trace4 = go.Line(x=df4["timestamp"], y=df4["value"], name="siggenroom2temp", line=dict(width=5))

trace5 = go.Line(x=df5["timestamp"], y=df5["value"], name="mavgroom1rhumrec", line=dict(width=5))
trace6 = go.Line(x=df6["timestamp"], y=df6["value"], name="mavgroom1temprec", line=dict(width=5))
trace7 = go.Line(x=df7["timestamp"], y=df7["value"], name="mavgroom1temppub", line=dict(width=5))
trace8 = go.Line(x=df8["timestamp"], y=df8["value"], name="mavgroom1rhumpub", line=dict(width=5))
trace9 = go.Line(x=df9["timestamp"], y=df9["value"], name="mavgroom2temprec", line=dict(width=5))
trace10 = go.Line(x=df10["timestamp"], y=df10["value"], name="mavgroom2rhumrec", line=dict(width=5))
trace11 = go.Line(x=df11["timestamp"], y=df11["value"], name="mavgroom2temppub", line=dict(width=5))
trace12 = go.Line(x=df12["timestamp"], y=df12["value"], name="mavgroom2rhumpub", line=dict(width=5))

trace13 = go.Line(x=df13["timestamp"], y=df13["value"], name="funcroom1temp", line=dict(width=5))
trace14 = go.Line(x=df14["timestamp"], y=df14["value"], name="funcroom1rhum", line=dict(width=5))
trace15 = go.Line(x=df15["timestamp"], y=df15["value"], name="funcroom2temp", line=dict(width=5))
trace16 = go.Line(x=df16["timestamp"], y=df16["value"], name="funcroom2rhum", line=dict(width=5))
trace17 = go.Line(x=df17["timestamp"], y=df17["value"], name="funcroom1ahum", line=dict(width=5))
trace18 = go.Line(x=df18["timestamp"], y=df18["value"], name="funcroom2ahum", line=dict(width=5))

data = [trace1, trace2, trace5, trace6, trace7, trace8, trace13, trace14, trace17]

fig = go.Figure(data=data)
fig.update_layout(title="data",
    xaxis_title="Timestamps",
    yaxis_title="Value",
    font_size=26)
fig.show()
