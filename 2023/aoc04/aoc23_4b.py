with open('aoc23_4b_input.txt') as f:
    data = f.readlines()

cards = []
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

    n = 0
    for h in hav:
        if h in win:
            n += 1
    cards.append(n)

have = [i for i in range(len(data))]
total = len(have)
while True:
    newhave = []
    for h in have:
        n = cards[h]
        newhave += [i+h+1 for i in range(n) if i+h+1 < len(cards)]
    if len(newhave) == 0:
        break
    total += len(newhave)
    have = newhave

print(total)