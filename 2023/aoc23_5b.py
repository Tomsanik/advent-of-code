def map_me(x, map):
    min_length = x[1]
    for d, s, l in map:
        if s <= x[0] < s+l:
            xl = min(x[1], l - (x[0] - s))
            return [d+x[0]-s, xl, x[2]]
        elif s > x[0]:
            if min_length > s-x[0]:
                min_length = s-x[0]
    return [x[0], min_length, x[2]]


def process(vals, m):
    if m == len(maps):
        res.append(vals)
        return
    new_vals = map_me(vals, maps[m])
    process(new_vals, m+1)
    if new_vals[1] < vals[1]:
        next_vals = [vals[0]+new_vals[1],
                     vals[1]-new_vals[1],
                     vals[2]+new_vals[1]]
        process(next_vals, m)


with open('aoc23_5b_input.txt') as f:
    data = f.readlines()

seeds = data[0][7:-1].split(' ')
seeds = [[int(seeds[2 * s]), int(seeds[2 * s + 1]), int(seeds[2 * s])] for s in range(len(seeds) // 2)]
print(seeds)

maps = []
map = []
for d in data[2:]:
    if '\n' in d:
        d = d[:-1]
    if d == '':
        maps.append(map)
        map = []
        continue
    if not d[0].isdigit():
        continue
    map.append([int(s) for s in d.split(' ')])
maps.append(map)

i = 0
min_loc = 0
q = 0
for seed in seeds:
    res = []
    process(seed, 0)
    for r in res:
        if min_loc > r[0] or min_loc == 0:
            min_loc = r[0]
    print(i, res)
    q += len(res)
    i += 1

print(min_loc)
print(q)