from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Training data
X = [
    [0, 0],
    [1, 1],
    [1, 0],
    [0, 1],
    [1, 2],
    [2, 1]
]

y = [0, 1, 1, 0, 1, 1]

print("Input Data:")
print(X)

print("Output Data:")
print(y)

# Create model
model = DecisionTreeClassifier(criterion="gini")

# Train model
model.fit(X, y)

print("Model trained")

# Test data
test = [[1, 0]]

print("Test Data:", test)

result = model.predict(test)

print("Prediction:", result)

# Accuracy check
score = model.score(X, y)

print("Accuracy:", score)

print("Decision Tree Completed")