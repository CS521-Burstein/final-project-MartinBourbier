#!/usr/bin/python3

from kaggle import KaggleApi
import os

if not (os.path.isdir("./dataset") and os.path.isfile("./dataset/application_record.csv") and os.path.isfile("./dataset/credit_record.csv")): 
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('rikdifos/credit-card-approval-prediction', path='./dataset', unzip=True)
else:
    exit(1)