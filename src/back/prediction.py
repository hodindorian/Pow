from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

def getColumnsForPredictionAndPredict(df,columns, columnGoal, algoOfPrediction):
    predictors = df[columns]
    target = df[columnGoal]

    if algoOfPrediction == "Linear Regression":
        model = LinearRegression()
    elif algoOfPrediction == "Random Forest":
        model = RandomForestRegressor(n_estimators=100)
    else:
        raise NameError("No method name : \"" + algoOfPrediction + "\"")

    model.fit(predictors, target)
    prediction = model.predict(predictors)
    return prediction

def correlation_matrix(df, columns):
    new_df = df[columns]
    correlations = new_df.corr()
    print(correlations)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(correlations, vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0,new_df.shape[1],1)
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(list(new_df))
    ax.set_yticklabels(list(new_df))
    return fig
