import pandas as pd


def csv_value():
    df = pd.read_csv('./data.csv')
    # print(df.head())

    #print all detail 
    # df.info()

    # Print number of missing value for each column
    # print(df.isna().sum())

    # Useless values
    # Off-Road Description         -> 156170
    # Municipality                 -> 152979
    # Related Non-Motorist         -> 166642
    # Non-Motorist Substance Abuse -> 167788
    # Circumstance                 -> 140746
    return df