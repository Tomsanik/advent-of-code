with open('input.txt') as f:
    data = f.readlines()

inst = data[0][:-1]
RL = {'L': 0, 'R': 1}

map = {}
here = []
for d in data[2:]:
    if '\n' in d:
        d = d[:-1]
    src = d.split(' ')[0]
    des = (d.split(' ')[2][1:-1], d.split(' ')[3][0:-1])
    map[src] = des
    if src[-1] == 'A':
        here.append(src)

n = 0
print(here)
idx = [0 for _ in range(len(here))]
while 0 in idx:
    for step in inst:
        n += 1
        for i in range(len(here)):
            dir = RL[step]
            here[i] = map[here[i]][dir]
            if here[i][-1] == 'Z':
                idx[i] = n//len(inst)
print(idx)

k = len(inst)
for i in idx:
    k *= i
print(k)
