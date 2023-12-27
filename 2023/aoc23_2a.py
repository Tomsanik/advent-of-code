with open('aoc23_2a_input.txt') as f:
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

    k = True
    for set in sets:
        cubes = set.split(', ')
        draw = {'red': 0, 'green': 0, 'blue': 0}
        for cube in cubes:
            x = cube.split(' ')
            draw[x[1]] = int(x[0])
        print(draw)

        for col in draw.keys():
            if draw[col] > q[col]:
                k = False
    if k:
        n += game
print(n)
