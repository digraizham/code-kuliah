import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('wholesale_dataset.csv')

# Check for missing values
if df.isnull().sum().any():
    df = df.fillna(df.mean())  # Fill missing values with mean

# Split dataset into features and target
X = df.drop('Region', axis=1)
y = df['Region']

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

# Initialize the SVM classifier
clf = svm.SVC()

# Train the classifier
clf.fit(X_train, y_train)

# Predict the target for the test data
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100}%')