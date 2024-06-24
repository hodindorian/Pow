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

def do_for_columns(df):
    for col_name in df:
        df[col_name] = function(df[col_name])


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

def csv_robust_normalize(df, col):
    # Calcul de la médiane et de l'IQR
    median = df[col].median()
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    # Application de la normalisation robuste
    normalized_column = (df[col] - median) / iqr
    df[col] = normalized_column
    return normalized_column

def handle_normalization(df, norm_method):
    if norm_method == "min-max":
        for col_name in df:
            df[col_name] = csv_norm_min_max(df, col_name)
        return df
    elif norm_method == "z-score":
        for col_name in df:
            df[col_name] = csv_standardisation_Z(df, col_name)
        return df
    elif norm_method == "robust":
        for col_name in df:
            df[col_name] = csv_robust_normalize(df, col_name)
        return df
    else:
        raise ValueError("Unknown method")
