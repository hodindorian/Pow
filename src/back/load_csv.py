import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler

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

def csv_norm_min_max(df, col):
    max = df[col].max()
    min = df[col].min()
    df[col] = (df[col] - min)/ (max - min)
    return df[col]

def csv_standardisation_Z(df, col):
    mean_col1 = df[col].mean()
    std_col1 = df[col].std()
    df[col] = (df[col] - mean_col1) / std_col1
    return df[col]

def robust_normalize_column(df, column_name):
    # Extract the column datas
    column_data = df[column_name].values.reshape(-1, 1)
    
    # Fit and transform the column datas
    scaler = RobustScaler()
    normalized_data = scaler.fit_transform(column_data)
    df[column_name] = normalized_data
    
    return normalized_data

def handle_normalization(df, norm_method):
    for col_name in df:
        if norm_method == "min-max":
            df[col_name] = csv_norm_min_max(df, col_name)
        elif norm_method == "z-score":
            df[col_name] = csv_standardisation_Z(df, col_name)
        elif norm_method == "robust":
            df[col_name] = robust_normalize_column(df, col_name)
        else:
            raise ValueError("Unknown method")
    return df
