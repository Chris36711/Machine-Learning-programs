from sklearn.linear_model import LinearRegression
import numpy as np

# size , rooms
X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 4],
    [2500, 4]
])

y = np.array([2, 3, 4, 5])

print("Training data")

print(X)

model = LinearRegression()

model.fit(X, y)

test = [[1800, 3]]

result = model.predict(test)

print("Predicted price =", result)