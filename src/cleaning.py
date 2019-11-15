import pandas as pd
import datetime
import re


def database():
    data = pd.read_csv('../input/Airplane_Crashes_and_Fatalities_Since_1908_20190820105639.csv')
    data1 = data[["Date","Operator"]]
    data1.dropna()
    data1['Date'] = pd.to_datetime(data1['Date'])
    data1['Year'] = data1['Date'].dt.year
    data1 = data1[data1['Year'] > 1969]
    data2 = data1[["Year","Operator"]].reset_index()
    data = data2
    data

