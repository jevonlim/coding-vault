import numpy as np

def least_squares(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x * x)
    sum_xy = np.sum(x * y)
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return a, b


np.random.seed(0)
x = np.random.rand(100) * 10
y = 4 * x + 3 + np.random.rand(100)
a, b = least_squares(x, y)

print(f"a: {a}, b: {b}")


