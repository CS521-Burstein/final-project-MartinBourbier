#!/usr/bin/python3

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.read_csv('./dataset/concatenated.csv')

le = LabelEncoder()

for label in data.columns.values:
    if data[label].dtype == 'object':
        data[label] = le.fit_transform(data[label])

grid = None
MODEL = "LOGREG"

# Logistic Regression model
if MODEL == "LOGREG":
    X = data.drop(['STATUS', 'ID', 'Unnamed: 0', 'MONTHS_BALANCE'], axis=1)
    y = data['STATUS']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = MinMaxScaler(feature_range=(0, 1))
    X_train_rescaled = scaler.fit_transform(X_train)
    X_test_rescaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=100)
    model.fit(X_train_rescaled, y_train)

    print("Logistic Regression model")
    print("Accuracy before optimizations:", model.score(X_test_rescaled, y_test))

    tolerance = [0.01, 0.001, 0.0001]
    max_iter = [100, 150, 200]

    params = dict(tol=tolerance, max_iter=max_iter)

    grid = GridSearchCV(estimator=model, param_grid=params, cv=5)

    X_rescaled = scaler.fit_transform(X)
    model_result = grid.fit(X_rescaled, y)

    score, best_params = model_result.best_score_, model_result.best_params_

    print("Best params:", best_params, "with accuracy:", score)

    model.set_params(**best_params)

# Decision Tree Classifier model
elif MODEL == "DTC":
    X = data.drop(['STATUS', 'ID', 'Unnamed: 0', 'MONTHS_BALANCE'], axis=1)
    y = data['STATUS']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    model = DecisionTreeClassifier()
    
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)

    print("Decision Tree Classifier model")
    print("Accuracy:", accuracy_score(y_test, y_pred))

# Random Forest Classifier model
elif MODEL == "RFTC":
    X = data.drop(['STATUS', 'ID', 'Unnamed: 0', 'MONTHS_BALANCE'], axis=1)
    y = data['STATUS']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # scaler = MinMaxScaler(feature_range=(0, 1))
    # X_train_rescaled = scaler.fit_transform(X_train)
    # X_test_rescaled = scaler.transform(X_test)
    model = RandomForestClassifier()

    # RF.fit(X_train_rescaled, y_train)

    # y_pred = RF.predict(X_test_rescaled)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Random Forest Classifier")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))

import pickle

s = pickle.dumps(model)

with open('model.pkl', 'wb') as f:
    f.write(s)

print(X.columns.values)