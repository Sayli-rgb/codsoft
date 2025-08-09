# ===== Iris Flower Classification =====
# This project will predict the type of Iris flower based on its measurements

# Step 1: Import required libraries
from sklearn.datasets import load_iris           # to get the iris dataset
from sklearn.model_selection import train_test_split  # to split data
from sklearn.linear_model import LogisticRegression   # model for prediction
from sklearn.metrics import accuracy_score       # to check accuracy

# Step 2: Load the iris dataset
iris = load_iris()      # load the data from sklearn
X = iris.data           # features (measurements of flowers)
y = iris.target         # target (flower type)

# Step 3: Split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Create and train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Check the accuracy
acc = accuracy_score(y_test, y_pred)
print("Model Accuracy:", acc)

# Step 7: Predict for new flower data
# Example: sepal length=5.1, sepal width=3.5, petal length=1.4, petal width=0.2
new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)
print("Predicted Flower Type:", iris.target_names[prediction][0])
