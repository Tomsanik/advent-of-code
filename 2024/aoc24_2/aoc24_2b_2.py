import numpy as np


def test(a):
    a = np.array(a)
    dx = (a - np.roll(a, 1))[1:]
    if np.all(dx < 0) or np.all(dx > 0):
        if np.all(abs(dx) < 4) and np.all(abs(dx) > 0):
            return True
    return False


with open('input.txt') as f:
    data = f.readlines()
res = 0
for line in data:
    line = line.strip('\n')
    a = [int(x) for x in line.split(' ')]
    print(f'{a}')
    if test(a):
        res += 1
        print(f'\tsafe')
    else:
        for i in range(len(a)):
            if test(a[:i]+a[i+1:]):
                res+=1
                print(f'\tsaved by removing {a[i]} on position {i}')
                break
print(res)