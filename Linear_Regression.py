import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Data
X=np.array([10, 9, 2, 15, 10, 16, 11, 16]).reshape(-1,1)
Y=np.array([15, 80, 10, 50, 45, 98, 38, 93])
# Model
model = LinearRegression()
model.fit(X, Y)
# Get values
a =model.intercept_
b =model.coef_[0]
print("Slope (b):", round(b,2))
print("Intercept (a):", round(a,2))
print("Regression Equation: Y =", round(a,2), "+", round(b,2), "X")
# Plot Graph
plt.scatter(X, Y, color='blue')
plt.plot(X, model.predict(X))
plt.xlabel("Hours Driving")
plt.ylabel("Risk Score")
plt.title("Linear Regression- Driving vs Risk")
plt.show()