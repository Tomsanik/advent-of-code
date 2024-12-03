import numpy as np

with open('input.txt') as f:
    data = f.readlines()

data = 'do()' + ''.join(data)

res = 0
dos = data.split('do()')
for do in dos:
    n = do.find("don't()")
    if n == -1:
        n = len(do)
    do = do[:n]
    dt = do.split('mul(')
    for d in dt:
        i = d.find(')')
        if i < 2:
            continue
        x = d[:i]
        y = x.split(',')
        if len(y) == 2:
            a, b = y
        else:
            continue
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            continue
        res += a*b
        # print(f'\t{res}')

print(res)
