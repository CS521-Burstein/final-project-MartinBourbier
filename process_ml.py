#!/usr/bin/python3

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn .metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.read_csv('./dataset/concatenated.csv')

le = LabelEncoder()

for label in data.columns.values:
    if data[label].dtype == 'object':
        data[label] = le.fit_transform(data[label])

MODEL = "RFTC"

if MODEL == "LOGREG":
    X = data.drop(['STATUS'], axis=1).drop(['ID'], axis=1)
    y = data['STATUS']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    scaler = MinMaxScaler(feature_range=(0, 1))
    X_train_rescaled = scaler.fit_transform(X_train)
    X_test_rescaled = scaler.transform(X_test)

    LogReg = LogisticRegression(max_iter=100)
    LogReg.fit(X_train_rescaled, y_train)

    print("Logistic Regression model")
    print("Accuracy before optimizations:", LogReg.score(X_test_rescaled, y_test))

    tolerance = [0.01, 0.001, 0.0001]
    max_iter = [100, 150, 200]

    params = dict(tol=tolerance, max_iter=max_iter)

    model = GridSearchCV(estimator=LogReg, param_grid=params, cv=5)

    X_rescaled = scaler.fit_transform(X)
    model_result = model.fit(X_rescaled, y)

    score, best_params = model_result.best_score_, model_result.best_params_

    print("Best params:", best_params, "with accuracy:", score)

    LogReg.set_params(**best_params)
elif MODEL == "DTC":
    X = data.drop(['STATUS'], axis=1).drop(['ID'], axis=1)
    y = data['STATUS']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    DT = DecisionTreeClassifier()
    
    DT.fit(X_train, y_train)
    
    y_pred = DT.predict(X_test)

    print("Decision Tree Classifier model")
    print("Accuracy:", accuracy_score(y_test, y_pred))

elif MODEL == "RFTC":
    X = data.drop(['STATUS'], axis=1).drop(['ID'], axis=1)
    y = data['STATUS']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    # scaler = MinMaxScaler(feature_range=(0, 1))
    # X_train_rescaled = scaler.fit_transform(X_train)
    # X_test_rescaled = scaler.transform(X_test)
    RF = RandomForestClassifier()

    # RF.fit(X_train_rescaled, y_train)

    # y_pred = RF.predict(X_test_rescaled)
    RF.fit(X_train, y_train)

    y_pred = RF.predict(X_test)

    print("Random Forest Classifier")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
