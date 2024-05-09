import yfinance as yf
from datetime import datetime, timedelta
from dataclasses import dataclass
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd
from pandas import DataFrame, Timestamp
import matplotlib.pyplot as plt


instruments        = pd.read_csv('data/nasdaq-instrument-list.csv')
instrument_symbols = instruments["Symbol"].to_list()
delta              = timedelta(days=-300)
today              = datetime.now()
in_groups_of_50    = np.array_split(instrument_symbols, 50)

for group_index in range(len(in_groups_of_50)):
  group = in_groups_of_50[group_index]
  print(f"group_index: {group_index}")
  data         = yf.download(" ".join(group), today + delta)
  data.columns = pd.MultiIndex.from_tuples([i[::-1] for i in data.columns])

  for instrument_index in range(len(group)):
    instrument_name = group[instrument_index]
    print(f"instrument_index: {instrument_index} - row {instrument_name}")
    try:
      print('saving')
      print('---')
      print(instrument_index)
      print('---')
      TEMP = data[instrument_name].copy(deep=True)
      TEMP = TEMP.dropna()
      TEMP.to_csv("data/instruments/"+instrument_name+".csv")
    except:
      print("Unaable to load data for {}".format(instrument_name))

