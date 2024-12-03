with open('input.txt') as f:
    data = f.readlines()

x, y = 0, 0
y0 = 0
for i in range(len(data)):
    d = data[i]
    if '\n' in d:
        data[i] = data[i][:-1]
    if 'S' in d:
        x = d.index('S')
        y = y0
    y0 += 1
pipe = [(x, y)]


def move(here, dx, dy):
    if dx == 1:
        if here == '7':
            dx, dy = 0, 1
        elif here == 'J':
            dx, dy = 0, -1
    elif dy == 1:
        if here == 'J':
            dx, dy = -1, 0
        elif here == 'L':
            dx, dy = 1, 0
    elif dx == -1:
        if here == 'F':
            dx, dy = 0, 1
        elif here == 'L':
            dx, dy = 0, -1
    elif dy == -1:
        if here == 'F':
            dx, dy = 1, 0
        elif here == '7':
            dx, dy = -1, 0
    return dx, dy


dx, dy = 0, 0
if data[y][x+1] in '-J7':
    dx = 1
elif data[y][x-1] in '-FL':
    dx = -1
elif data[y+1][x] in '|LJ':
    dy = 1
elif data[y-1][x] in '|F7':
    dy = -1

x += dx
y += dy
here = data[y][x]
pipe.append([x, y])
while here != 'S':
    dx, dy = move(here, dx, dy)
    x += dx
    y += dy
    here = data[y][x]
    pipe.append((x, y))

for y in range(len(data)):
    for x in range(len(data[0])):
        if (x, y) in pipe:
            continue
        temp = list(data[y])
        temp[x] = '.'
        data[y] = ''.join(temp)
    print(data[y])

p = 0
n = 0
x, y = 0, 0
for d in data:
    for t in d:
        if t == '.' and p % 2 == 1:
            n += 1
        elif t in '|LJ':
            p += 1
        x += 1
    y += 1
    x = 0
print(n)

