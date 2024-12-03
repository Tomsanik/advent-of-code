with open('input.txt') as f:
    data = f.readlines()

for d in data:
    if '\n' in d:
        d = d[:-1]
    springs, groups = d.split(' ')
    while '..' in springs:
        springs = springs.replace('..', '.')
    springs = list(springs.split('.'))
    while '' in springs:
        springs.remove('')

    groups = groups.split(',')
    for i, g in enumerate(groups):
        groups[i] = int(g)

    if springs[0][0] == '#':
        springs[0][:groups[0]-1] = '#'

    print(springs, groups)

