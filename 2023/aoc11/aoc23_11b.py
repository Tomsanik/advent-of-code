def calc(a):
    total, di, pred = 0, 0, 0
    n = sum(a)
    for i in range(len(a)):
        if a[i] == 0:
            di += 1e6-1
            continue
        za = n-pred-a[i]
        total += ((pred - za) * (i + di)) * a[i]
        pred += a[i]
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

