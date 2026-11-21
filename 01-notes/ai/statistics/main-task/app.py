import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 8, 9, 13])
print(np.polyfit(x, y, 1))

#CLOSED FORM
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x * x)
n = len(x)

a = ((n * sum_xy) - (sum_y * sum_x)) / (n * sum_x2 - (sum_x) ** 2)
b = (sum_y - a * sum_x) / n

print(f"a: {a}, b: {b}")

#GRADIENT DESCENT

a = 0
b = 0
lr = 2
cost_history = []

for i in range(50):
    gradient_a = 2 * a * sum_x2 + 2 * b * sum_x - 2 * sum_xy
    gradient_b = 2 * a * sum_x + 2 * b * n - 2 * sum_y

    cost = 0
    for i,j in zip(x,y):
        cost = cost + (a * i + b - j) ** 2
    cost_history.append(cost)

    a = a - gradient_a * lr
    b = b - gradient_b * lr

print(cost_history)



