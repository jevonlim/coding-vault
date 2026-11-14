import numpy as np

population = np.random.normal(170, 10, 100000)

means_20 = []
for i in range(200):
    sample = np.random.choice(population, 20)
    means_20.append(np.average(sample))

means_200 = []
for i in range(200):
    sample = np.random.choice(population, 200)
    means_200.append(np.average(sample))

print(f"SD of Means 20: {np.std(means_20)}")
print(f"SD of Means 200: {np.std(means_200)}")