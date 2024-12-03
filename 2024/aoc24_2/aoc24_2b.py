'''
Tohle nefunguje, verze 2 je hloupejsi a funkcni:D
'''
import numpy as np


def test(dy):
    a, b, c, d = None, None, None, None
    plus = np.count_nonzero(dy > 0)
    zero = np.count_nonzero(dy == 0)
    minus = np.count_nonzero(dy < 0)
    oor = np.count_nonzero(np.abs(dy) > 3)  # out of range

    if plus > 1 and minus > 1:
        print(f'!!\tc\t {plus} {zero} {minus} {oor}')
    else:
        print(f'\tc\t {plus} {zero} {minus} {oor}')

    if plus == 1:
        a = np.where(dy > 0)[0][0]
    if zero == 1:
        b = np.where(dy == 0)[0][0]
    if minus == 1:
        c = np.where(dy < 0)[0][0]
    if oor == 1:
        d = np.where(np.abs(dy) > 3)[0][0]

    s = '\tp\t'
    idx = []
    for e in [a, b, c, d]:
        if e is None:
            s += ' -'
        else:
            s += ' '+str(e)
            idx.append(e)
    print(s)
    if len(idx) == 1:
        sgn = 1 if plus > minus else -1
        return idx[0], sgn
    else:
        return -1, 0



with open('input.txt') as f:
    data = f.readlines()

res_comp = 0
res = 0
for line in data:
    k = False
    line = line.strip('\n')
    a = line.split(' ')
    a = np.array([int(x) for x in a])
    dx = (a-np.roll(a, 1))[1:]
    if np.all(dx<0) or np.all(dx>0):
        if np.all(abs(dx) < 4) and np.all(abs(dx) > 0):
            # print(a, f'safe\t{dx}')
            k = True
            res_comp += 1

    if not k:
        print(a, f'unsafe\t{dx}')
        p, pm = test(dx)

        # print(p)
        if p == -1:
            continue
        elif p == 0:
            # print(f'\tsaved by removing {a[p]} on position {p}')
            res += 1
        elif p == len(dx)-1:
            # print(f'\tsaved by removing {a[p + 1]} on position {p + 1}')
            res += 1
        elif 0 < np.abs(dx[p] + dx[p + 1]) <= 3 and (dx[p] + dx[p + 1])*pm > 0:
            print('\t', p, dx[p], dx[p+1])
            print(f'\tsaved by removing {a[p+1]} on position {p+1}')
            res += 1
        elif 0 < np.abs(dx[p-1] + dx[p]) <= 3 and (dx[p-1] + dx[p])*pm > 0:
            print('\t', p, dx[p-1], dx[p])
            print(f'\tsaved by removing {a[p]} on position {p}')
            res += 1
print(f'completely safe: {res_comp}')
print(res+res_comp)