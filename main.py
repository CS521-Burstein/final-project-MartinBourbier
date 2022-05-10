import pickle
import numpy as np

import pandas as pd
from sklearn.preprocessing import LabelEncoder

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Welcome! Please enter your information below:")

def amount_income():
    while True:
        try:
            val = float(input("Enter your annual income: "))
        except:
            print("Please enter a valid input.")
            continue
        break
    
    return val

def income_type():
    while True:
        answer = input("Enter your income type (Working/Commercial associate/Other): ")

        if answer == "Working" or answer == "Commercial associate" or answer == "Other":
            break

        print("Please enter a valid input.")
        
    return answer

def education_type():
    while True:
        answer = input("Enter your education type (Secondary/Higher education/Other): ")

        if answer == "Secondary" or answer == "Higher education" or answer == "Other":
            break
        
        print("Please enter a valid input.")
        
    return answer

def family_status():
    while True:
        answer = input("Enter your family status (Single/Married/Civil Marriage/Separated/Other): ")

        if answer == "Single" or answer == "Married" or answer == "Civil Marriage" or answer == "Separeted" or answer == "Other":
            break
        
        print("Please enter a valid input.")
        
    return answer

def housing_type():
    while True:
        answer = input("Enter your housing type ('House / apartment'/'Rented apartment'/'Municipal "
                                "apartment'/'With parents'/Other): ")
                            
        if answer == "House / apartment" or answer == "Rented apartment" or answer == "Municipal apartment" or answer == "With parents" or answer == "Other":
            break
        
        print("Please enter a valid input.")
        
    return answer

def occupation_type():
    while True:
        answer = input("Enter your occupation type (Student/Professional/Other): ")
        
        if answer == "Student" or answer == "Professional" or answer == "Other":
            break
        
        print("Please enter a valid input.")
        
    return answer

def fam_members():
    while True:
        try:
            val = int(input("Enter the number of household family members: "))
        except:
            print("Please enter a valid input.")
            continue
        break

    return val

def age():
    while True:
        try:
            val = float(input("Enter your age: "))
        except:
            print("Please enter a valid input.")
            continue
        break
    
    return val

def years_employed():
    while True:
        try:
            val = float(input("Enter the number of years employed: "))
        except:
            print("Please enter a valid input.")
            continue
        break
    
    return val

values = {
    'CODE_GENDER': [1 if input("Enter your gender (M/F): ") == "M" else 0],
    'FLAG_OWN_CAR': [1 if input("Do you own a car (Y/N)? ") == "Y" else 0],
    'FLAG_OWN_REALTY': [1 if input("Do you own realty (Y/N)? ") == "Y" else 0],
    'AMT_INCOME_TOTAL': [amount_income()],
    'NAME_INCOME_TYPE': [income_type()],
    'NAME_EDUCATION_TYPE': [education_type()],
    'NAME_FAMILY_STATUS': [family_status()],
    'NAME_HOUSING_TYPE': [housing_type()],
    'OCCUPATION_TYPE': [occupation_type()],
    'CNT_FAM_MEMBERS': [fam_members()],
    'AGE': [age()],
    'YEARS_EMPLOYED': [years_employed()]
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