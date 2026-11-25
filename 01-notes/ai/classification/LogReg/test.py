import numpy as np

rng = np.random.default_rng(0)
idx = rng.permutation(20)
train_idx = idx[:15]
test_idx =  idx[15:]
print(idx)