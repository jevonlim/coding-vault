import numpy as np

population = np.random.normal(170, 10, 100000)

means_20 = []
for i in range(1000):
    sample = np.random.choice(population, 20)   # pick 20 random people
    means_20.append(...)                        # the mean of this sample

means_200 = []
# same loop, with sample size 200

print(np.std(means_20))
print(np.std(means_200))