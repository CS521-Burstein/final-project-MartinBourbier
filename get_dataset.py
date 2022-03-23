import os

dataset_dir = './dataset'
dataset_name = 'dog-breed-identification'
kaggle_api_call = 'kaggle competitions download -c dog-breed-identification'

if os.path.isdir(dataset_dir):
    # Avoid downloading the dataset if it already exists
    exit()

os.system(kaggle_api_call)
os.system(f'mkdir {dataset_dir}')
os.system(f'unzip {dataset_name}.zip -d {dataset_dir}')
os.system(f'rm {dataset_name}.zip')
