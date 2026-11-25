import numpy as np
# from sklearn.linear_model import LogisticRegression

def sigma(z):
    return 1 / (1 + (np.e)**(-z))

def train(x, y, lr=0.1, steps=1000):
    length = len(y)
    n, d = x.shape
    w = np.zeros(d)
    b = 0
    for _ in range(steps):
        z = x @ w + b
        p = sigma(z)
        grad_w = (1/length) * (x.T @ (p-y))
        grad_b = np.mean(p-y)
        w = w - lr * grad_w
        b = b - lr * grad_b 
    return w,b

protein  = np.array([520, 610, 680, 750, 820, 900, 560, 640, 700, 780, 850, 950, 480, 590, 720, 800, 880, 1000, 660, 740])
exercise = np.array([90, 200, 120, 160, 240, 180, 60, 140, 220, 100, 130, 260, 40, 170, 80, 210, 150, 300, 190, 110])
height   = np.array([161.5, 167.3, 171.2, 171.5, 182.2, 176.8, 161.2, 170.5, 173.1, 172.9, 172.9, 187.1, 154.4, 169.3, 167.4, 179.4, 174.9, 192.5, 169.6, 170.7])

# Define initial parameters
X = np.column_stack([protein, exercise])
median = np.median(height)
y = (height > median).astype(float)

# Store the accuracy for training and testing
train_accs = []
test_accs = []

# Repeat the 5 sample split over and over and get its average
for seed in range(20):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(20)
    train_idx = idx[:15]
    test_idx =  idx[15:]

    # Statistics from train data only
    mu = X[train_idx].mean(axis=0)
    std = X[train_idx].std(axis=0)

    # Apply same mu and std to train data
    x_train = (X[train_idx] - mu) / std
    y_train = y[train_idx]

    # TRAINING AREA
    w, b = train(x_train, y_train)

    # TRAIN ACCURACY
    train_pred = (sigma(x_train @ w + b) > 0.5).astype(float)
    train_acc = np.mean(train_pred == y_train) * 100
    train_accs.append(train_acc)
    print(f"Train {seed} Accuracy: {train_acc}%")

    # TEST AREA
    x_test = (X[test_idx] - mu) / std # apply mu and std to test data
    y_test = y[test_idx]

    # TEST ACCURACY
    test_pred = (sigma(x_test @ w + b) > 0.5).astype(float)
    test_acc = np.mean(test_pred == y_test) * 100
    test_accs.append(test_acc)
    print(f"Test {seed} Accuracy: {test_acc}%")


train_acc_avg = np.mean(train_accs)
train_acc_std = np.std(train_accs)
test_acc_avg = np.mean(test_accs)
test_acc_std = np.std(test_accs)

print(f"Average Training Accuracy: ({train_acc_avg:.1f} ± {train_acc_std:.1f})%")
print(f"Average Test Accuracy: ({test_acc_avg:.1f}% ± {test_acc_std:.1f})%")
# # Compare with sklearn library
# model = LogisticRegression(C=1e6, max_iter=1000)
# model.fit(X, y)

# w_true = model.coef_ # the weights w, shape (1, 2)
# b_true = model.intercept_ # the bias b, shape (1,)

# print(f"My w and b: {w} and {b}")
# print(f"True w and b: {w_true} and {b_true}")