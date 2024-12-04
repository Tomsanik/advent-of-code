import numpy
import numpy as np


def transpose(A):
    B = ['' for _ in range(len(A[0]))]
    for line in A:
        for i in range(len(line)):
            B[i] += line[i]
    return B


with open('input.txt') as f:
    data = f.readlines()
data2 = []
for d in data:
    d = d.strip('\n')
    data2.append(d)
data = data2

res = 0
for d in data:
    for s in ['XMAS', 'SAMX']:
        a = ''.join(d.split(s))
        res += int((len(d)-len(a))/4)

N = transpose(data)
for n in N:
    for s in ['XMAS', 'SAMX']:
        a = ''.join(n.split(s))
        res += int((len(n)-len(a))/4)

N1, N2 = [], []
for i, d in enumerate(data):
    d1 = 'O'*len(d[i:]) + d +'O'*i
    d2 = 'O'*i + d + 'O'*len(d[i:])
    N1.append(d1)
    N2.append(d2)

N1 = transpose(N1)
N2 = transpose(N2)

for n in N1:
    for s in ['XMAS', 'SAMX']:
        a = ''.join(n.split(s))
        res += int((len(n)-len(a))/4)

for n in N2:
    for s in ['XMAS', 'SAMX']:
        a = ''.join(n.split(s))
        res += int((len(n)-len(a))/4)

print(res)

