# ===== Titanic Survival Prediction =====
# This project predicts if a passenger survived the Titanic disaster or not

# Step 1: Import required libraries
import pandas as pd          # for reading and handling data
import numpy as np           # for numerical operations
import seaborn as sns        # for data visualization
import matplotlib.pyplot as plt  # for plotting graphs
from sklearn.model_selection import train_test_split   # for splitting the dataset
from sklearn.linear_model import LogisticRegression    # machine learning model
from sklearn.metrics import accuracy_score             # to check model accuracy

# Step 2: Load the dataset (train.csv should be in the same folder as this code)
data = pd.read_csv("train.csv")

# Step 3: Remove columns we don't need
data = data.drop(columns=['Cabin', 'Name', 'Ticket'], axis=1)

# Step 4: Fill missing values
data['Age'] = data['Age'].fillna(data['Age'].mean())  # fill missing ages with average
data['Embarked'] = data['Embarked'].fillna(data['Embarked'].mode()[0])  # most common value

# Step 5: Convert text values to numbers
data.replace({
    'Sex': {'male': 0, 'female': 1},
    'Embarked': {'S': 0, 'C': 1, 'Q': 2}
}, inplace=True)

# Step 6: Split data into features (X) and target (y)
X = data.drop(columns=['Survived', 'PassengerId'])  # passenger details
y = data['Survived']  # survived or not

# Step 7: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 8: Create and train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 9: Predict and check accuracy
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Model Accuracy:", acc)

# Step 10: Predict survival for a new passenger
# Example passenger: class=3, male, age=22, siblings=1, parents=0, fare=7.25, embarked=S(0)
new_passenger = [[3, 0, 22.0, 1, 0, 7.25, 0]]
result = model.predict(new_passenger)
print("Survival Prediction:", "Survived" if result[0] == 1 else "Not Survived")
# Step 10: Predict survival for a new passenger (with column names to remove warning)
new_passenger = pd.DataFrame([[3, 0, 22.0, 1, 0, 7.25, 0]],
                             columns=X.columns)
result = model.predict(new_passenger)
print("Survival Prediction:", "Survived" if result[0] == 1 else "Not Survived")


