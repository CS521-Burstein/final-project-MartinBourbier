#!/usr/bin/python3

import pandas as pd

YEAR = 365.2425

data_folder = "./dataset"

application_record = pd.read_csv(f"{data_folder}/application_record.csv")
credit_record = pd.read_csv(f"{data_folder}/credit_record.csv")

# DAYS_BIRTH -> AGE

application_record['AGE'] = -application_record['DAYS_BIRTH'] / YEAR
application_record.drop(columns="DAYS_BIRTH", axis=1, inplace=True)

# DAYS_EMPLOYED -> YEARS_EMPLOYED
application_record['YEARS_EMPLOYED'] = -application_record['DAYS_EMPLOYED'] / YEAR
application_record.loc[application_record['YEARS_EMPLOYED'] <= 0, 'YEARS_EMPLOYED'] = 0
application_record.drop(columns="DAYS_EMPLOYED", axis=1, inplace=True)

print(application_record.columns)