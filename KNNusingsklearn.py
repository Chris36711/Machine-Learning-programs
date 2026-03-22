from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Training data
X = [
    [1], [2], [3], [4], [5], [6]
]

y = [0, 0, 0, 1, 1, 1]

print("Input Data:")
print(X)

print("Output Data:")
print(y)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X, y)

print("Model trained")

# Test data
test = [[2.5]]

print("Test Data:", test)

result = model.predict(test)

print("Prediction:", result)

# Accuracy check
score = model.score(X, y)

print("Accuracy:", score)

print("KNN Completed")