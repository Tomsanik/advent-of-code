with open('aoc23_2b_input.txt') as f:
    data = f.readlines()

q = {'red': 12, 'green': 13, 'blue': 14}
n = 0
for d in data:
    if '\n' in d:
        d = d[:-1]
    a = d.find(' ')
    b = d.find(':')
    game = int(d[a + 1:b])
    print('Game', game)
    d = d[b + 2:]
    print(d)
    sets = d.split('; ')

    max_draw = {'red': 0, 'green': 0, 'blue': 0}
    for set in sets:
        cubes = set.split(', ')
        for cube in cubes:
            x = cube.split(' ')
            if int(x[0]) > max_draw[x[1]]:
                max_draw[x[1]] = int(x[0])
    print(max_draw)
    y = 1
    for p in max_draw.values():
        y *= p
    n += y

print(n)
