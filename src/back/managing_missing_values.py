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
    missing_columns = data.columns[data.isnull().any()].tolist()
    
    for col in missing_columns:
        missing_data = data[data[col].isnull()]
        complete_data = data[~data[col].isnull()]
        if missing_data.empty or complete_data.empty:
            continue
        X_complete = complete_data.drop(columns=missing_columns)
        y_complete = complete_data[col]
        X_missing = missing_data.drop(columns=missing_columns)
        if X_missing.shape[0] > 0.5 * data.shape[0]:
            continue
        model = LinearRegression()
        model.fit(X_complete, y_complete)
        y_pred = model.predict(X_missing)
        data.loc[df[col].isnull(), col] = y_pred
        
    return data


"""    
    Parameters:
    - data: Pandas DataFrame with the data
    - method: Method to handle missing values ('drop', 'mean', 'median', 'mode', 'knn', 'regression')
    - n_neighbors: Number of neighbors to use for KNN imputation (only used if method='knn')
"""
def handle_missing_values(data, method, n_neighbors=5):
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