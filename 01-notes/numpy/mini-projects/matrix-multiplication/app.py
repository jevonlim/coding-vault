import numpy as np

def mat_mul(a,b):
    if a.ndim != 2 or b.ndim != 2:
        raise ValueError("Inputs must be 2D arrays or above")
    if (a.shape[1] != b.shape[0]):
        raise ValueError("Matrix multiplication can't be executed")

    result = []
    for i in range(a.shape[0]):
        temp = []
        for j in range(b.shape[1]):
            temp2 = 0
            for k in range(a.shape[1]):
                temp2 += a[i,k] * b[k,j]
            temp.append(temp2)
        result.append(temp)

    return result
    

a = np.random.rand(2, 4)
b = np.random.rand(4, 2)

print(np.allclose(mat_mul(a,b), np.matmul(a,b)))
