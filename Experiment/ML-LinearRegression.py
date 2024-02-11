import numpy as np
import matplotlib.pyplot as plt

# Generate a sample dataset
np.random.seed(0)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Plot the dataset
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sample Dataset')
plt.show()

# Implementing linear regression with gradient descent
class LinearRegressionGD:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.theta_0 = 0
        self.theta_1 = 0

    def predict(self, x):
        return self.theta_0 + self.theta_1 * x

    def compute_cost(self, x, y):
        m = len(y)
        return (1/(2*m)) * np.sum((self.predict(x) - y)**2)

    def fit(self, x, y):
        m = len(y)
        for _ in range(self.n_iterations):
            prediction = self.predict(x)
            d_theta_0 = (1/m) * np.sum(prediction - y)
            d_theta_1 = (1/m) * np.sum((prediction - y) * x)
            self.theta_0 -= self.learning_rate * d_theta_0
            self.theta_1 -= self.learning_rate * d_theta_1

# Create a linear regression model instance
model = LinearRegressionGD()
model.fit(x, y)

# Plotting the results
plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red')  # regression line
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.show()

# Output the parameters
model.theta_0, model.theta_1
