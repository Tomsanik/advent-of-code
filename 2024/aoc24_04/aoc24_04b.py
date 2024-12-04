"""Funguje pouze pro čtvercové vstupy"""

def transpose(A):
    B = ['' for _ in range(len(A[0]))]
    for line in A:
        for i in range(len(line)):
            B[i] += line[i]
    return B

def coord12(x, y, w):
    y2 = y + 2 * x - w + 1
    return x, y2

def findAs(p):
    q = p.split('A')
    a = []
    k = 0
    for i, qq in enumerate(q):
        k += len(qq)
        a.append(k+i)
    a = a[:-1]
    return a


data = []
with open('input.txt') as f:
    for line in f:
        data.append(line.strip('\n'))

N1, N2 = [], []
for i, d in enumerate(data):
    d1 = 'O'*len(d[i:]) + d +'O'*(i+1)
    N1.append(d1)
    d2 = 'O'*(i+1) + d + 'O'*len(d[i:])
    N2.append(d2)

N1 = transpose(N1)
N2 = transpose(N2)
w = len(N1[0])

for n1, n2 in zip(N1, N2):
    print(n1, n2)

res = 0
for j, n in enumerate(N1):
    idx = findAs(n)
    for x in idx:
        r = n[x - 1:x + 2]
        if r in ['MAS', 'SAM']:
            x1, y1 = coord12(x, j, w)
            if x1 <= 0:
                continue
            r = N2[y1][x1-1:x1+2]
            if r in ['MAS', 'SAM']:
                res += 1
print(res)

