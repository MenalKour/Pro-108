import random
import plotly.express as px
import csv
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv("phone.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
fig.show()