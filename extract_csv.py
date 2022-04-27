#!/usr/bin/python3
import numpy as np
import pandas as pd
YEAR = 365.2425

data_folder = "./dataset"

application_record = pd.read_csv(f"{data_folder}/application_record.csv",index_col="ID")
credit_record = pd.read_csv(f"{data_folder}/credit_record.csv", index_col="ID")

# DAYS_BIRTH -> AGE

application_record['AGE'] = -application_record['DAYS_BIRTH'] / YEAR
application_record.drop(columns="DAYS_BIRTH", axis=1, inplace=True)

# DAYS_EMPLOYED -> YEARS_EMPLOYED
application_record['YEARS_EMPLOYED'] = -application_record['DAYS_EMPLOYED'] / YEAR
application_record.loc[application_record['YEARS_EMPLOYED'] <= 0, 'YEARS_EMPLOYED'] = 0
application_record.drop(columns="DAYS_EMPLOYED", axis=1, inplace=True)


#DROPPING CNT_CHILDERN COLUMN
application_record.drop(columns='CNT_CHILDREN',axis=1,inplace=True)

#DROP USERS WHO HAVE MORE THAN 10 FAMILY MEMBERS

application_record.drop(application_record[application_record['CNT_FAM_MEMBERS']>10].index, inplace=True)
# drop flag_mobile since it is always true
application_record.drop('FLAG_MOBIL', axis=1, inplace=True)

print(application_record.columns)

# Replace X and C characters with -1
credit_record.replace('X', -1, inplace=True)
credit_record.replace('C', -1, inplace=True)

# Change data type of STATUS column from string to integer
credit_record['STATUS'] = credit_record['STATUS'].astype(int)

# Normalize value to be = 1 if STATUS >= 1
credit_record.loc[credit_record['STATUS'] >= 1, 'STATUS'] = 1
#change status=-1 to status=0
credit_record.loc[credit_record['STATUS']<=-1,'STATUS']=0

# Keep only the highest value when ID's have duplicates
df = pd.DataFrame(credit_record.groupby(['ID'])['STATUS'].agg(max)).reset_index()

concat_1 = pd.merge(application_record, df, on=['ID'])
# Extract how many months account has been open for
start_df=pd.DataFrame(credit_record.groupby(['ID'])['MONTHS_BALANCE'].agg(min)).reset_index()
start_df['MONTHS_BALANCE']=-start_df['MONTHS_BALANCE']
concat = pd.merge(concat_1, start_df, on=['ID'])

concat['OCCUPATION_TYPE'].replace(np.nan, 'Other', inplace=True)
concat['FLAG_OWN_CAR'].replace(['Y', 'N'], [1, 0], inplace=True)
concat['CODE_GENDER'].replace(['M', 'F'], [1, 0], inplace=True)
concat['FLAG_OWN_REALTY'].replace(['Y', 'N'], [1, 0], inplace=True)
concat['NAME_INCOME_TYPE'] = concat.NAME_INCOME_TYPE.astype('category').cat.codes
concat['NAME_EDUCATION_TYPE'] = concat.NAME_EDUCATION_TYPE.astype('category').cat.codes
concat['NAME_FAMILY_STATUS'] = concat.NAME_FAMILY_STATUS.astype('category').cat.codes
concat['NAME_HOUSING_TYPE'] = concat.NAME_HOUSING_TYPE.astype('category').cat.codes
concat['OCCUPATION_TYPE'] = concat.OCCUPATION_TYPE.astype('category').cat.codes

concat.CNT_FAM_MEMBERS = concat.CNT_FAM_MEMBERS.astype(int)

# Write merge result to the file
concat.to_csv(f'{data_folder}/concatenated.csv')