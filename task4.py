# ===== Sales Prediction using Linear Regression =====
# This project predicts product sales based on advertising spend

# Step 1: Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Step 2: Create a small sample dataset
data = {
    'TV': [230.1, 44.5, 17.2, 151.5, 180.8],
    'Radio': [37.8, 39.3, 45.9, 41.3, 10.8],
    'Newspaper': [69.2, 45.1, 69.3, 58.5, 58.4],
    'Sales': [22.1, 10.4, 9.3, 18.5, 12.9]
}
df = pd.DataFrame(data)

# Step 3: Split into features (X) and target (y)
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Step 4: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Check accuracy (R² score)
accuracy = r2_score(y_test, y_pred)
print("Model Accuracy (R² Score):", round(accuracy * 100, 2), "%")

# Step 8: Predict for new ad spend data
new_data = [[200, 40, 60]]  # TV=200, Radio=40, Newspaper=60
predicted_sales = model.predict(new_data)
print("Predicted Sales:", round(predicted_sales[0], 2))
