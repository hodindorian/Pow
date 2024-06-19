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


def replace_with_mean(data):
    return data.apply(lambda col: col.fillna(col.mean()) if col.dtype.kind in 'biufc' else col)

def replace_with_median(data):
    return data.apply(lambda col: col.fillna(col.median()) if col.dtype.kind in 'biufc' else col)

def replace_with_mode(data):
    return data.apply(lambda col: col.fillna(col.mode()[0]) if col.mode().size > 0 else col)

def impute_with_knn(data, n_neighbors=5):
    imputer = KNNImputer(n_neighbors=n_neighbors)
    return pd.DataFrame(imputer.fit_transform(data), columns=data.columns)

def impute_with_regression(data):
    for column in data.columns:
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
def handle_missing_values(data, method, n_neighbors=5):

    data = drop_high_null_percentage(data)
    data = convert_categorical_to_numeric(data)    
    if method == 'mean':
        return replace_with_mean(data)
    elif method == 'median':
        return replace_with_median(data)
    elif method == 'mode':
        return replace_with_mode(data)
    elif method == 'knn':
        return impute_with_knn(data, n_neighbors=n_neighbors)
    elif method == 'regression':
        return impute_with_regression(data)
    else:
        raise ValueError("Unknown method")

