with open('input.txt') as f:
    data = f.readlines()

x, y = 0, 0
for d in data:
    if '\n' in d:
        d = d[:-1]
    if 'S' in d:
        x = d.find('S')
        break
    y += 1


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
n = 1
while here != 'S':
    dx, dy = move(here, dx, dy)
    x += dx
    y += dy
    here = data[y][x]
    n += 1
print(n//2)
