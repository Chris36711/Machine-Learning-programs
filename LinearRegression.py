from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5]])

y = np.array([2, 4, 6, 8, 10])

print("Input X =", X)

print("Output y =", y)

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction for 6 = ", prediction)

print("Coefficient =", model.coef_)

print("Intercept =", model.intercept_)