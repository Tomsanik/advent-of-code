def calc(a):
    total, di, pred = 0, 0, 0
    n = sum(a)
    for i, ai in enumerate(a):
        if ai == 0:
            di += 1
            continue
        total += ((pred - (n-pred-ai)) * (i + di)) * ai
        pred += ai
    return total


with open('input.txt') as f:
    data = f.readlines()

xs, ys = [0] * len(data[0]), [0] * len(data)
y = 0
for d in data:
    x = -1
    while '#' in d[x+1:]:
        x = d.find('#', x+1)
        xs[x] += 1
        ys[y] += 1
    y += 1
print(calc(xs) + calc(ys))

