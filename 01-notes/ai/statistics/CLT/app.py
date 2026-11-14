import numpy as np
import matplotlib.pyplot as plt

data = np.random.exponential(1,100000)
sample_means = []


for i in range(3000):
    sample = np.random.choice(data, 200)
    sample_means.append(np.mean(sample))


plt.hist(sample_means, bins=40)
plt.xlabel("sample mean")
plt.ylabel("count")
plt.title("Means of 5,000 samples (n = 30)")
plt.show()
