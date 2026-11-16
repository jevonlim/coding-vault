import numpy as np

def fit_line(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x * x)
    sum_xy = np.sum(x * y)
    a = (((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_xx) - (sum_x)**2))
    b = (sum_y - a * sum_x) / n

    return a, b

np.random.seed(0)
x = np.random.rand(100) * 10
y = 5 * x + 4 + np.random.randn(100)

a, b = fit_line(x, y)

print(f"a = {a}, b = {b}")