import numpy as np

with open('input.txt') as f:
    data = f.readlines()

a, b = [], []
for d in data:
    x, y = d.split('   ')
    if '\n' in y:
        y = y[:-1]
    print(x, y)
    a.append(int(x))
    b.append(int(y))

a.sort()
b.sort()

a = np.array(a)
b = np.array(b)

dx = np.sum(np.abs(a-b))
print(dx)
