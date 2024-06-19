import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
import numpy as np
import load_csv as l 

def convert_categorical_to_numeric(data):
    for column in data.columns:
        if data[column].nunique() <= 15:
            data[column] = data[column].astype('category')
            data[column] = data[column].cat.codes.replace(-1, np.nan) + 1
        else:
            data = data.drop(column, axis=1)
    return data

def drop_high_null_percentage(data, threshold=0.5):
    missing_percentage = data.isnull().mean()
    data = data.loc[:, missing_percentage <= threshold]
    return data



def replace_with_mean(data, column):
    data[column] = data[column].fillna(data[column].mean())
    return data

def replace_with_median(data, column):
    data[column] = data[column].fillna(data[column].median())
    return data

def replace_with_mode(data, column):
    mode_value = data[column].mode()
    if not mode_value.empty:
        data[column] = data[column].fillna(mode_value[0])
    return data

def impute_with_knn(data, column, n_neighbors=5):
    imputer = KNNImputer(n_neighbors=n_neighbors)
    data[[column]] = imputer.fit_transform(data[[column]])
    return data

def impute_with_regression(data, column):
    if data[column].isnull().sum() > 0:
        train_data = data[data[column].notna()]
        test_data = data[data[column].isna()]
        if not train_data.empty and not test_data.empty:
            regressor = LinearRegression()
            regressor.fit(train_data.drop(column, axis=1), train_data[column])
            data.loc[data[column].isna(), column] = regressor.predict(test_data.drop(column, axis=1))
    return data


"""    
    Parameters:
    - data: Pandas DataFrame with the data
    - method: Method to handle missing values ('drop', 'mean', 'median', 'mode', 'knn', 'regression')
    - n_neighbors: Number of neighbors to use for KNN imputation (only used if method='knn')
"""
def handle_missing_values(data, method, column, n_neighbors=5):

    data = drop_high_null_percentage(data)
    data = convert_categorical_to_numeric(data)
        
    if method == 'mean':
        return replace_with_mean(data, column)
    elif method == 'median':
        return replace_with_median(data, column)
    elif method == 'mode':
        return replace_with_mode(data, column)
    elif method == 'knn':
        return impute_with_knn(data, column, n_neighbors=n_neighbors)
    elif method == 'regression':
        return impute_with_regression(data, column)
    elif method == 'drop_high_null':
        return drop_high_null_percentage(data)
    else:
        raise ValueError("Unknown method")



data = l.return_csv('./data.csv')
cleaned_data = handle_missing_values(data, method='mode', column='Route Type')
print(cleaned_data)
