from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def getColumnsForPredictionAndPredict(df,columns, columnGoal, algoOfPrediction):
    predictors = df[columns]
    target = df[columnGoal]
    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.2, random_state=42)

    if algoOfPrediction == "Régression Linéaire":
        model = LinearRegression()
    elif algoOfPrediction == "Forêt Aléatoire":
        model = RandomForestRegressor(n_estimators=100)   
    else:
        raise NameError("No method name : \"" + algoOfPrediction + "\"")

    model.fit(X_train, y_train)
    return model.predict(X_test)