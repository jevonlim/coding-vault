import numpy as np
from scipy import stats

nose   = np.array([5.0, 6.2, 4.5, 7.1, 5.8, 6.5, 4.8, 7.5, 5.3, 6.8])
leg    = np.array([20.0, 25.0, 22.0, 24.0, 28.0, 21.0, 26.0, 23.0, 27.0, 25.0])
length = np.array([58.0, 62.0, 55.0, 75.0, 60.0, 64.0, 57.0, 70.0, 53.0, 72.0])

w, b = np.polyfit(nose, length, 1) # 1 represents the degree polymonial being fitted, which is a line
predicted = w * nose + b
ss_single = np.sum((predicted - length)**2)

n = len(length)
X = np.column_stack([nose, leg, np.ones(n)]) # put them in columns
w = np.linalg.lstsq(X, length, rcond=None)[0]
predicted = X @ w
ss_multiple = np.sum((predicted - length)**2)

F_value = (ss_single - ss_multiple) / (ss_single / (n-3))

if F_value < 1:
    print(f"F Value: {F_value:.2f}, NOT WORTH OF TIME TO COLLECT FURTHER DATA RELATED TO LEG LENGTH TO PREDICT BODY LENGTH")