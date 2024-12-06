import numpy as np

def draw_map(m):
    for line in m:
        print(''.join(line))


def copy(m):
    m2 = []
    for line in m:
        m2.append(line.copy())
    return m2

directions = {0: (-1, 0), 1: (0, -1), 2: (1, 0), 3: (0, 1)}
dirs = ['<', '^', '>', 'v']

nn = 0
mapa = []
with open('input.txt') as f:
    for i, line in enumerate(f):
        line = list(line.strip('\n'))
        mapa.append(line)
        # print(line)
        nn += len(line)
        for j, d in enumerate(dirs):
            if d in line:
                x, y = line.index(d), i
                dir = j
# print(nn)
trace = [[], []]
# print(x, y, dir)
w, h = len(mapa[0]), len(mapa)
konec = False
while True:
    dx, dy = directions[dir]
    while mapa[y][x] != '#':
        # mapa[y][x] = 'X'
        if (x, y) not in trace[0]:
            trace[0].append((x, y))
            trace[1].append(dir)
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

# mapa2 = mapa.copy()
# for (x, y), dir in zip(trace[0], trace[1]):
#     mapa2[y][x] = dirs[dir]
# for line in mapa2:
#     print(line)
# input()

trace2 = [(x, y, dir) for (x, y), dir in zip(trace[0], trace[1])]

adds = []
mapa0 = copy(mapa)
print(f's={len(trace2)}')
for i in range(len(trace2)):
    print(f'{i/len(trace2):.1%}')
    mapa = copy(mapa0)
    x, y, dir = trace2[i]
    mapa[y][x] = 'O'
    # draw_map(mapa)
    konec = False
    trace3 = []
    while True:
        # draw_map(mapa)
        dx, dy = directions[dir]
        while mapa[y][x] not in ['#', 'O']:
            mapa[y][x] = dirs[dir]
            if (x, y, dir) in trace3:
                konec = True
                adds.append((x, y))
                print('\t', x,y)
                break
            trace3.append((x, y, dir))
            x += dx
            y += dy
            if x >= w or x < 0 or y >= h or y < 0:
                konec = True
                break
        x -= dx
        y -= dy
        if not konec:
            dir = (dir + 1) % 4
            if mapa[y+dx][x+dx] == 'O':
                ox, oy, od = x, y, dir
                print(ox, oy, dir)

        else:
            break

print(len(adds))
