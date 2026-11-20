import numpy as np

def my_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def my_var(data):
    total = 0
    mean = my_mean(data)
    for x in data:
        total += (x - mean) ** 2
    return total / (len(data) - 1)

def my_std(data):
    var = my_var(data)
    return (var) ** 0.5

data = np.random.normal(0, 1, 100)

high = my_mean(data) + 2 * my_std(data)
low = my_mean(data) - 2 * my_std(data)

for x in data:
    if (x < low or x > high):
        print(x)

