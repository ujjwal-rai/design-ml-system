import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Get file paths from the command line arguments
dataset_path = sys.argv[1]
features_path = sys.argv[2]

# Load CSV files
dataset = pd.read_csv(dataset_path)
features_desc = pd.read_csv(features_path)

# Print the feature description for context (can be enhanced)
print("Feature Description:")
print(features_desc)

# Assume the last column is the target variable for simplicity
X = dataset.iloc[:, :-1]  # All columns except the last one
y = dataset.iloc[:, -1]   # The last column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Output the classification report
report = classification_report(y_test, y_pred)
print("Logistic Regression Report:")
print(report)
