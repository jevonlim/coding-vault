def my_mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def my_var(data):
    total = 0
    mean = my_mean(data)
    for x in data:
        total += (x - mean) ** 2
    return total / (len(data) - 1)

def my_std(data):
    var = my_var(data)
    return (var) ** 0.5

def my_covariance(x,y):
    total = 0
    x_mean = my_mean(x)
    y_mean = my_mean(y)
    for i,j in zip(x,y):
        total += (i-x_mean) * (j-y_mean)
    return total / (len(x) - 1)

def my_correlation(x,y):
    covarience = my_covariance(x,y)
    x_std = my_std(x)
    y_std = my_std(y)
    return covarience / (x_std * y_std)


x = [-2,-1,0,1,2]
y = [0,-5,-10,-20,-30]

print(f"Covariance: {my_covariance(x,y)}")
print(f"Correlation: {my_correlation(x,y)}")
