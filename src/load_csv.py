#!/usr/bin/env python3
import pandas as pd


def csv_value():
    df = pd.read_csv('./data.csv')
    print(df.head())
    return df
