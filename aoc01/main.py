with open('input.txt', encoding='UTF-8') as f:
    lines = f.readlines()

elves = []
cal = 0
for l in lines:
    if l != '\n':
        l.strip()
        cal += int(l)
    else:
        elves.append(cal)
        cal = 0

max = [0, 0, 0]
for e in elves:
    k = 0
    flag = False
    for i in range(3):
        if flag:
            p = max[i]
            max[i] = k
            k = p
        elif e > max[i]:
            flag = True
            k = max[i]
            max[i] = e
mm = 0
for m in max:
    mm += m

print(mm)
