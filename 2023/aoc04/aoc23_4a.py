with open('aoc23_4a_input.txt') as f:
    data = f.readlines()

points = 0
for d in data:
    if '\n' in d:
        d = d[:-1]
    d = d.replace('  ', ' ')
    a = d.find(' ')
    b = d.find(': ')
    card = int(d[a:b])

    d = d[b+2:]
    k = d.find(' | ')
    win = d[:k].split(' ')
    hav = d[k+3:].split(' ')

    point = 0.5
    for h in hav:
        if h in win:
            point *= 2
    points += int(point)

print(points)