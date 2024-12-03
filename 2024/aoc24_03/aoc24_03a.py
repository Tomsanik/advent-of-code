import numpy as np

with open('input.txt') as f:
    data = f.readlines()

data = ''.join(data)

res = 0
muls = data.split('mul(')
for d in muls:
    i = d.find(')')
    if i < 2:
        # print(d)
        continue
    x = d[:i]
    # print(x)
    y = x.split(',')
    if len(y) == 2:
        a, b = y
    else:
        continue
    try:
        if ' ' in a or ' ' in b:
            continue
        a = int(a)
        b = int(b)
    except ValueError:
        continue
    res += a*b

print(res)
