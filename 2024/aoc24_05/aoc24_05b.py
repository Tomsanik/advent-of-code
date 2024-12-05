rules = {}
updates = []
kont = False
with open('input.txt') as f:
    for line in f:
        if line == '\n':
            kont = True
            continue
        if kont:
            updates.append(line.strip('\n').split(','))
        else:
            a = line.strip('\n').split('|')
            if a[0] in rules.keys():
                rules[a[0]].append(a[1])
            else:
                rules[a[0]] = [a[1]]

bad_upd = []
res = 0
for update in updates:
    kont = True
    i = 0
    while i < len(update):
        page = update[i]
        idx1, idx2 = -1, -1
        if page in rules.keys():
            idx1 = update.index(page)
            idx_min = idx1
            for r in rules[page]:
                if r in update:
                    idx2 = update.index(r)
                    idx_min = min(idx2, idx_min)
            if idx_min != idx1:
                update[idx1], update[idx_min] = update[idx_min], update[idx1]
                i = idx_min
                kont = False
        i += 1

    if not kont:
        bad_upd.append(update)
        n = len(update) // 2
        res += int(update[n])
print(res)
