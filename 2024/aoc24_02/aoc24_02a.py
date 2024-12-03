import numpy as np

with open('input.txt') as f:
    data = f.readlines()

res = 0
for line in data:
    k = False
    line = line.strip('\n')
    a = line.split(' ')
    a = np.array([int(x) for x in a])
    dx = (np.roll(a, 1)-a)[1:]
    if np.all(dx<0) or np.all(dx>0):
        if np.all(abs(dx) < 4) and np.all(abs(dx) > 0):
            print(a, 'safe')
            k = True
            res += 1
    if not k:
        print(a, 'unsafe')
print(res)