import pandas as pd
import numpy as np


def load_data(data):
   '''
   input : csv file
   output : numpy
   '''
   df = pd.read_csv(data, names=['open','high','low','close'])
   data = df['open']
   data = np.array(data)

   return data


def load_predict_data(data):
   '''
   input : csv file
   output : numpy
   '''
   df = pd.read_csv(data, names=['open'])
   data = np.array(df)

   return data   