with open('input.txt') as f:
    w = 0
    mapa = ''
    for line in f:
        line = line.strip()
        w = len(line)
        mapa += line

antenas = {}
for i, c in enumerate(mapa):
    if c != '.' and c != '#':
        if c in antenas.keys():
            antenas[c].append(i)
        else:
            antenas[c] = [i]
nodes = []
for freq in antenas.keys():
    ants = antenas[freq]
    if len(ants) == 1:
        continue
    for i, x in enumerate(ants[:-1]):
        for y in ants[i+1:]:
            k = 0
            kont = True
            while kont:
                kont = False
                a = x - k*(y-x)
                b = y + k*(y-x)
                # print(x, y, a, b)
                if 0 <= a < len(mapa):
                    if k*(y // w - x//w) == x//w - a//w:
                        kont = True
                        if a not in nodes:
                            nodes.append(a)
                if 0 <= b < len(mapa):
                    if k*(y // w - x//w) == b//w - y//w:
                        kont = True
                        if b not in nodes:
                            nodes.append(b)

                k += 1
print(antenas)
for n in nodes:
    mapa = mapa[:n]+'x'+mapa[n+1:]
    print(n // w, n % w)
n = 0
while n <= len(mapa):
    print(mapa[n:n+w])
    n += w
print(nodes)
print(len(nodes))

