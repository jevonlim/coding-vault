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

data = [1,2,30,34,400,-5]

print(f"STD is {my_std(data)}")

