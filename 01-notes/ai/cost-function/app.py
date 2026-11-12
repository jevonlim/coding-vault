w = 10
learning_rate = 0.001

for step in range(20):
    gradient = 2 * (w - 3)
    w = w - gradient * learning_rate
    print(step, ":", w)