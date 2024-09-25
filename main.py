import numpy as np
import joblib

# Generate some dummy data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term (X0 = 1) for the intercept
X_b = np.c_[np.ones((100, 1)), X]  # Add x0 = 1 to each instance

# Calculate the parameters using the Normal Equation: theta = (X^T * X)^(-1) * X^T * y
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Save the model (theta parameters)
joblib.dump(theta_best, 'linear_regression_model.joblib')
