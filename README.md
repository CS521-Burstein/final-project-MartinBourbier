# Credit Card Approval Prediction

CS521 final project. Collaborators: Martin Bourbier, Jenny Hopkins, and Aigerim Dussikenova

Dataset link: `https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction`

Based on personal information, the system predicts whether an individual would be approved for a credit card or not.

We worked on the project in the "dev" branch.

Instructions:
   1. In the directory you are running the code from, create a folder called ./dataset 
   2. To run get_dataset.py correctly, you need to create an account on kaggle and make sure to download your 
      kaggle.json file. You can find resources online to do this. 
   3. Run the get_dataset.py, followed by the extract_csv.py scripts locally. This will generate a file called 
   concatenated.csv in the dataset folder, which will then be used to generate the reports and graphs in 
   exploring_data.ipynb and MLmodel_visualizations. Each cell in the ipynb files should be run sequentially.
   4. To have user interaction with the model (predict credit card approval results based on a series of questions), 
      run main.py from your terminal and answer the questions.