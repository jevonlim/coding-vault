import numpy as np

def my_dot(a,b):
    sum = 0
    if len(a) != len(b):
        raise ValueError("vectors don't match")
        
    for i in range(len(a)):
        sum = sum + a[i] * b[i]
    return sum

a = np.array([10101,101,1])
b = np.array([1,2,3])
W
print(my_dot(a,b))
