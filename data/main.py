from preprocessing import time_window, handcrafted_features
from utils.functions import *
from utils.load_datasets import load_MHEAL, load_OPPT_I
import numpy as np
import argparse
import os
import pandas as pd

#OVERLAPPING: 0.25 0.5 0.75
#WINDOW_SIZE: 1S 2S

parser = argparse.ArgumentParser(description='Specify window arguments')
parser.add_argument('-ws', '--window_size', type=int,
                    help='Samples per window')
parser.add_argument('-ov', '--overlapping', type=float,
                    help='Percentage of samples (in %) between previous and current window.')
parser.add_argument('-c', '--by_client', default=True,
                    action='store_false',
                    help='Return data by clients (True or False)')
parser.add_argument('-ds', '--answer', default="U", type =str,
                    help='Specify the dataset name')


args = parser.parse_args()

overlapping = args.overlapping/100
window_size = args.window_size

functions = [mean, rango, std, max, min, var, median]

if "preprocessed_data" not in os.listdir():
  os.mkdir("preprocessed_data")
ds_answer=args.answer
if ds_answer=="U":
  sensor,data=load_MHEAL(subjects=True)
  subject_features=[]
  n=len(data)

  names = [list(data[i]["Subject"])[0] for i in range(n)]

  for i in range(n):
    features, labels, sensor_names = time_window(data[i], window_size , overlapping)
    
    h_features, column_names = handcrafted_features(features, 
                                                  functions,
                                                  ["mean", "rango", "std", "max", "min","var", "median"],
                                                  sensor_names)
    df_processed = pd.DataFrame(h_features)
    
    df_processed.columns = column_names
    df_processed["Activity"] = labels
    df_processed["Subject"] = names[i]
    df_processed["Sensor"] = sensor
    subject_features.append(df_processed)

  df_final = subject_features[0]
  for i in range(1,n):
      df_final = pd.concat([df_final, subject_features[i]])
  df_final.reset_index(inplace=True, drop=True)
  contador=1
  num_vari=len(df_final)
  df_final['ID'] = None
  df_final['DTS'] = None
  for j in range(num_vari):
    df_final.loc[j, 'ID'] = ("MHE_{}".format(contador))
    df_final.loc[j, 'DTS'] = "Mhealth"
    contador +=1
  df_final=df_final.reindex(columns=['ID', 'DTS', 'Subject','Activity','Sensor'] + list(df_final.columns.difference(['ID', 'DTS', 'Subject','Activity','Sensor'])))
  df_final.to_csv("preprocessed_data/{}_{}_{}.csv".format("Mhealth", window_size, int(args.overlapping)), index=False)
