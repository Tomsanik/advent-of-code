with open('input.txt') as f:
    data = f.readlines()

inst = data[0][:-1]
RL = {'L': 0, 'R': 1}

map = {}
for d in data[2:]:
    if '\n' in d:
        d = d[:-1]
    src = d.split(' ')[0]
    des = (d.split(' ')[2][1:-1], d.split(' ')[3][0:-1])
    map[src] = des

n = 0
here = 'AAA'
print(here)
end = False
while not end:
    for step in inst:
        dir = RL[step]
        here = map[here][dir]
        n += 1
        if here == 'ZZZ':
            end = True
print(n)
