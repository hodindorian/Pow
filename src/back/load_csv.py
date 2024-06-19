import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

def return_csv(path):
    df = pd.read_csv(path)
    return df

def csv_value(df):
    #print all detail 
    df.info()
    # Print number of missing value for each column
    print(df.isna().sum())
    # Useless values


def csv_check(df):
    for col in df:
        print("-"*12)
        print(col)
        print("-"*12)
        print(df[col].unique())


def csv_norm_min_max(df,col):
    maValue = df[col].max
    miValue = df[col].min
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    return df

def csv_standardisation_Z(df,col):
    mean_col1 = df[col].mean()
    std_col1 = df[col].std()
    df[col] = (df[col] - mean_col1) / std_col1
    return df[col]

