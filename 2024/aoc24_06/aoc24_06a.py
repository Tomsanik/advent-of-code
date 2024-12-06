import numpy as np

directions = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}
dirs = ['<', '^', '>', 'v']

mapa = []
with open('input.txt') as f:
    for i, line in enumerate(f):
        line = list(line.strip('\n'))
        mapa.append(line)
        for j, d in enumerate(dirs):
            if d in line:
                x, y = line.index(d), i
                dir = j

w, h = len(mapa[0]), len(mapa)
konec = False
while True:
    dx, dy = directions[dir]
    while mapa[y][x] != '#':
        mapa[y][x] = 'X'
        x += dx
        y += dy
        if x >= w or x < 0 or y >= h or y < 0:
            konec = True
            break
    x -= dx
    y -= dy
    if not konec:
        dir = (dir+1) % 4
    else:
        break
    # for line in mapa:
    #     print(line)

mapa = np.array(mapa)
print(np.count_nonzero(mapa=='X'))




