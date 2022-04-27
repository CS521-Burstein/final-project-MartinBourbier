# Credit Card Approval Prediction

CS521 final project. Collaborators: Martin Bourbier, Jenny Hopkins, and Aigerim Dussikenova

Dataset link: `https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction`

Based on personal information, the system predicts whether an individual would be approved for a credit card or not.

We are currently working in the "dev" branch.

Brief instructions:
1. In the directory you are running the code from, create a folder called ./dataset
2. Run the get_dataset.py, followed by the extract_csv.py scripts locally, which will generate a file called concatenated.csv, which will then be used to generate the reports and graphs in exploring_data.ipynb. 

Updates as of 4/27/22:
1. We have edited the data to fit our needs (for example, dropped some columns that do not add value to the models or exhibit collinearity, and changed the status column to binary values of 0 = no late payments -> ACCEPT and 1 = late payments -> DENY).
2. We are exploring different visualizations to make better sense of the data (see ipynb file). 
***Question for Professor Burstein: does it make sense to drop many of the "status = 0" rows to have data that is more 50/50 Accept vs. Deny? 
3. We have implemented a Logistic Regression model (accuracy 0.882) and a Decision Tree Classifier model (accuracy 0.841). Next steps
will be to create more visualizations and gain more insight from the ML models, and explore other models. 
