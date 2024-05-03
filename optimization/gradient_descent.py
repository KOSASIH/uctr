import numpy as np

def gradient_descent(objective_function, initial_point, learning_rate, num_iterations):
    x = initial_point
    for _ in range(num_iterations):
        gradient = np.array(objective_function(x, grad=True))
        x -= learning_rate * gradient
    return x
