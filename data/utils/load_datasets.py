import pandas as pd
import numpy as np

def load_MHEAL(subjects=False):
    df = pd.read_csv("../data/datasets/MHEALTHDATASET.csv", sep=",")
    df.sort_values(by="ID_MHE", key=lambda x: x.str.split("_").str[-1].astype(int),inplace=True)
    df.reset_index(drop=True, inplace=True)
    sensor=df["Sensor"].loc[0]
    df.drop(["ID_MHE","Sensor"],axis=1,inplace=True)
    if subjects:
	    
        unique_subjects = np.unique(df["Subject"])
        tmp = []
        for subject in unique_subjects:
            tmp2 = df[df["Subject"]==subject].copy()
            #tmp2.drop(["Subject"], axis=1, inplace=True)
            tmp2 =tmp2[tmp2["Activity_Number"] != "MHE_A_00"]
            tmp.append(tmp2)
        #tmp[2].head()
        return sensor,tmp
    else:
	    raise Exception("Not implemented yet")

def load_OPPT_I(subjects=False):
    df = pd.read_csv("../data/datasets/Opportunity_IMU.csv", sep=",")
    df.sort_values(by=['ID_OPTY'], key=lambda x: x.str.split("_").str[-1].astype(int),inplace=True)
    df.reset_index(drop=True, inplace=True)
    sensor=df["Sensor"].loc[0]
    df.drop(["ID_OPTY","Locomotion","Sensor"],axis=1,inplace=True)
    if subjects:
	    
        unique_subjects = np.unique(df["Subject"])
        tmp = []
        for subject in unique_subjects:
            tmp2 = df[df["Subject"]==subject].copy()
            #tmp2.drop(["Subject"], axis=1, inplace=True)
            tmp2 =tmp2[tmp2["Activity_Number"] != "OPTY_A_00"]
            tmp.append(tmp2)
        #tmp[2].head()
        return sensor,tmp
    else:
	    raise Exception("Not implemented yet")
    
    
    

