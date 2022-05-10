import pickle
import numpy as np

import pandas as pd
from sklearn.preprocessing import LabelEncoder

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Welcome! Please enter your information below:")

values = {
    'CODE_GENDER': [1 if input("Enter your gender (M/W): ") == "M" else 0],
    'FLAG_OWN_CAR': [1 if input("Do you own a car (Y/N)? ") == "Y" else 0],
    'FLAG_OWN_REALTY': [1 if input("Do you own realty (Y/N)? ") == "Y" else 0],
    'AMT_INCOME_TOTAL': [float(input("Enter your annual income: "))],
    'NAME_INCOME_TYPE': [input("Enter your income type (Working/Commercial associate/Other): ")],
    'NAME_EDUCATION_TYPE': [input("Enter your education type (Secondary/Higher education/Other): ")],
    'NAME_FAMILY_STATUS': [input("Enter your family status (Single/Married/Other): ")],
    'NAME_HOUSING_TYPE': [input("Enter your housing type ('House / appartment'/Other): ")],
    'FLAG_WORK_PHONE': [1 if input("Do you have a work phone (Y/N)? ") == "Y" else 0],
    'FLAG_PHONE': [1 if input("Do you have a phone (Y/N)? ") == "Y" else 0],
    'FLAG_EMAIL': [1 if input("Do you have an email (Y/N)? ") == "Y" else 0],
    'OCCUPATION_TYPE': [input("Enter your occupation type (Student/Professional/Other): ")],
    'CNT_FAM_MEMBERS': [int(input("Enter the number of family members: "))],
    'AGE': [float(input("Enter your age: "))],
    'YEARS_EMPLOYED': [float(input("Enter the number of years employed: "))]
}

# Create a dataframe with the input values
data = pd.DataFrame.from_dict(values)

le = LabelEncoder()

data['OCCUPATION_TYPE'].replace(np.nan, 'Other', inplace=True)
data['FLAG_OWN_CAR'].replace(['Y', 'N'], [1, 0], inplace=True)
data['CODE_GENDER'].replace(['M', 'F'], [1, 0], inplace=True)
data['FLAG_OWN_REALTY'].replace(['Y', 'N'], [1, 0], inplace=True)
data['NAME_INCOME_TYPE'] = data.NAME_INCOME_TYPE.astype('category').cat.codes
data['NAME_EDUCATION_TYPE'] = data.NAME_EDUCATION_TYPE.astype('category').cat.codes
data['NAME_FAMILY_STATUS'] = data.NAME_FAMILY_STATUS.astype('category').cat.codes
data['NAME_HOUSING_TYPE'] = data.NAME_HOUSING_TYPE.astype('category').cat.codes
data['OCCUPATION_TYPE'] = data.OCCUPATION_TYPE.astype('category').cat.codes

data.CNT_FAM_MEMBERS = data.CNT_FAM_MEMBERS.astype(int)

for label in data.columns.values:
    if data[label].dtype == 'object':
        data[label] = le.fit_transform(data[label])

output = model.predict(data)[0]

print("Your credit card was", "approved!" if output == 1 else "denied.")