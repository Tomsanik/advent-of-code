import numpy as np


# mapa = [list(line.strip()) for line in open('input.txt')]
mapa = []
antenas = {}
with open('input.txt') as f:
    h = 0
    w = 0
    for line in f:
        line = line.strip()
        w = len(line)
        for j, c in enumerate(line):
            if c != '.':
                if c in antenas.keys():
                    antenas[c].append(np.array([h, j]))
                else:
                    antenas[c] = [np.array([h, j])]
        h += 1
print(antenas)
print(w, h)
nodes = []
for freq in antenas.keys():
    if freq == '#':
        continue
    if len(antenas[freq]) == 1:
        continue
    ants = antenas[freq]
    for a in range(len(ants)-1):
        A = ants[a]
        for b in range(a+1, len(ants)):
            B = ants[b]
            node = [2*A-B, 2*B-A]
            for n in node:
                if 0 > n[0] or n[0] >= w or n[1] < 0 or n[1] >= h:
                    continue
                if np.any(node == n):
                    nodes.append(n)
print(nodes)
print(len(nodes))

