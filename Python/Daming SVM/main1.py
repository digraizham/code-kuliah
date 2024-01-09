import pandas as pd
from sklearn.svm import SVC

# 1. Read training data
train_data = pd.read_csv('07DataSet_LDA_Training.csv')

# 2. Train the Linear-SVM model
target_column = 'Prime_Sport'
features = train_data.drop(target_column, axis=1)
target = train_data[target_column]

linear_svm = SVC(kernel='linear')
linear_svm.fit(features, target)

# 3. Read scoring data
scoring_data = pd.read_csv('07DataSet_LDA_Scoring.csv')

# 4. Use the trained model for scoring
scoring_predictions = linear_svm.predict(scoring_data)

# 5. Add predictions to the scoring data
scoring_data['predicted_target'] = scoring_predictions

# 6. Save the scoring results to a new CSV file
scoring_data.to_csv('hasil_deployment.csv', index=False)

# Display the first few rows of the scoring results
print("Scoring Results:")
print(scoring_data.head())
