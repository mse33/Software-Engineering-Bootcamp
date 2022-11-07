import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn import linear_model

# Determine gradient from x and y values.
def determineGradient(dx_train, dy_train):
    return ((np.mean(dx_train) * np.mean(dy_train) 
            - np.mean(dx_train * dy_train))
            / ((np.mean(dx_train) ** 2) - (np.mean(dx_train ** 2))))

# Determine Y intercept from x and y values.
def determineYIntercept(dx_train, dy_train):
    return (np.mean(dy_train) - determineGradient(dx_train, dy_train) 
           * np.mean(dx_train))

# Calculate the predicted y value for a given x value.
def makePrediction(x_value):
    return (gradient * x_value) + y_intercept


# Load data to variables and split the data
diabetes = load_diabetes()
d_X = diabetes.data[:, np.newaxis, 2].squeeze()
dx_train = d_X[:-20]
dy_train = diabetes.target[:-20]
dx_test = d_X[-20:]
dy_test = diabetes.target[-20:]

# Get gradiet and y intercept
gradient = determineGradient(dx_train, dy_train)
y_intercept = determineYIntercept(dx_train, dy_train)

print(gradient)
print(y_intercept)

# Scatter points on graph and plot regression line.
plt.scatter(dx_train, dy_train, label="Train Data",  c='r')
plt.scatter(dx_test, dy_test, label="Test Data",  c='g')
plt.plot(dx_test, makePrediction(dx_test), label="Best Fit Line", c='b')
plt.legend()

# Display graph
plt.show()