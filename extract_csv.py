#!/usr/bin/python3

import pandas as pd
YEAR = 365.2425

data_folder = "."
#data_folder = "./dataset"

application_record = pd.read_csv(f"{data_folder}/application_record.csv",index_col="ID")
credit_record = pd.read_csv(f"{data_folder}/credit_record.csv", index_col="ID")

# DAYS_BIRTH -> AGE

application_record['AGE'] = -application_record['DAYS_BIRTH'] / YEAR
application_record.drop(columns="DAYS_BIRTH", axis=1, inplace=True)

# DAYS_EMPLOYED -> YEARS_EMPLOYED
application_record['YEARS_EMPLOYED'] = -application_record['DAYS_EMPLOYED'] / YEAR
application_record.loc[application_record['YEARS_EMPLOYED'] <= 0, 'YEARS_EMPLOYED'] = 0
application_record.drop(columns="DAYS_EMPLOYED", axis=1, inplace=True)

print(application_record.columns)

df=pd.merge(application_record, credit_record, on='ID', how='left')
df=df.drop_duplicates()


# Replace X and C characters with -1
df.STATUS = df.apply(lambda x: -1 if x.STATUS=='C' or x.STATUS == 'X' or pd.isna(x.STATUS) else x.STATUS, axis=1)
# Change data type of STATUS column from string to integer
df.STATUS = df.STATUS.astype('int')

# Write merge result to the file
df.to_csv('concatenated.csv')
