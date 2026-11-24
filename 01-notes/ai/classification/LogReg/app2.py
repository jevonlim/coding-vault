import numpy as np
from sklearn.linear_model import LogisticRegression

def sigma(z):
    return 1 / (1 + (np.e)**(-z))

protein  = np.array([520, 610, 680, 750, 820, 900, 560, 640, 700, 780, 850, 950, 480, 590, 720, 800, 880, 1000, 660, 740])
exercise = np.array([90, 200, 120, 160, 240, 180, 60, 140, 220, 100, 130, 260, 40, 170, 80, 210, 150, 300, 190, 110])
height   = np.array([161.5, 167.3, 171.2, 171.5, 182.2, 176.8, 161.2, 170.5, 173.1, 172.9, 172.9, 187.1, 154.4, 169.3, 167.4, 179.4, 174.9, 192.5, 169.6, 170.7])

w = np.zeros(2)
b = 0.0
median = np.median(height)
y = (height > median).astype(float)
X = np.column_stack([protein, exercise])
X = (X - X.mean(axis=0)) / X.std(axis=0) # axis = 0, means do it per column
losses = []
n = len(protein)
lr = 0.1

for i in range(20000):
    z = X @ w + b
    p = sigma(z)
    loss = -np.mean(y * np.log(p) + (1-y) * np.log(1-p))
    losses.append(loss)
    gradient_w = (1/n) * (X.T @ (p-y))
    gradient_b = np.mean(p-y)

    w = w - lr * gradient_w
    b = b - lr * gradient_b


z = X @ w + b
p = sigma(z)
p_final = p > 0.5
accuracy = np.mean(p_final == y) * 100

print(f"Accuracy is {accuracy}%")


clf = LogisticRegression(penalty=None, max_iter=1000).fit(X, y)

print("sklearn w:", clf.coef_[0], " b:", clf.intercept_[0])
print("your    w:", w, " b:", b)