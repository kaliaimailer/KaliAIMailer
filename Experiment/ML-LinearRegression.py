from sklearn.linear_model import LinearRegression
import numpy as np

# Generate a synthetic sequence (for example, numbers from 1 to 100)
X = np.arange(1, 101).reshape(-1, 1)  # Features (reshape is required to make it a 2D array)
y = np.arange(2, 102).reshape(-1, 1)  # Labels (next number in the sequence)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict the next number after the last number in our sequence
next_number_prediction = model.predict([[101]])
print(f"The predicted next number is: {next_number_prediction[0][0]}")
