import numpy as np

def my_mean(sample):
    sum = 0
    length = len(sample)
    for i in sample:
        sum += i
    return sum / length

def my_sd(sample):
    mean = my_mean(sample)
    length = len(sample)
    total = 0
    for i in sample:
        total += (i-mean)**2
    return (total / (length - 1))**0.5


population = np.random.normal(3, 1, 10000)

sample = np.random.choice(population, 10)
length = len(sample)

se_1 = my_sd(sample) / (length)**0.5

means = []
for i in range(5000):
    sample_2 = np.random.choice(sample, 10)
    means.append(my_mean(sample_2))

se_2 = my_sd(means)

print(f"Standard Error 1: {se_1}, Standard Error 2: {se_2}")




