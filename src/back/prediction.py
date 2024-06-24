from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

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
    return model.predict(predictors)
