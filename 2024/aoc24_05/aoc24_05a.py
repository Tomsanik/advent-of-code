def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val in value:
            return key
    return None


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

correct = []
bad_upd = []
for update in updates:
    kont = True
    for page in update:
        idx1, idx2 = -1, -1
        if page in rules.keys():
            if not kont:
                break
            for r in rules[page]:
                if r in update:
                    idx1 = update.index(page)
                    idx2 = update.index(r)
                    if idx2 < idx1:
                        correct.append(False)
                        kont = False
                        break
                    print(page, idx1, rules[page], idx2)
        # if page in rules.values():
        #     key = get_key(rules, page)
        #     if key not in update:
        #         continue
        #     idx1 = update.index(key)
        #     idx2 = update.index(page)
        #     print('val', page, idx1, key, idx2)
    if kont:
        correct.append(True)

print(correct)
res = 0
for u, c in zip(updates, correct):
    if c:
        n = len(u)//2
        res += int(u[n])
print(res)
