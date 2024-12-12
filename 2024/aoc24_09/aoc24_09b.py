zapis = open('input.txt').readline().strip()
# print(zapis)

disk = []
i = 0
for z in zapis:
    if i % 2 == 1:
        disk += ['.']*int(z)
    else:
        disk += [i//2]*int(z)
    i += 1
# disk = ''.join(disk)
print(disk)

mezery = []
cisla = []
k = False
for i in range(len(zapis)):
    if k:
        mezery.append(int(zapis[i]))
    else:
        cisla.append(int(zapis[i]))
    k = not k

print(zapis)
# print(cisla)
# print(mezery)
res = ['' for _ in range(sum([int(c) for c in zapis]))]
mezery2 = mezery.copy()
cisla2 = cisla.copy()

for j, n in enumerate(cisla[::-1]):
    j = len(cisla)-j-1
    for i, m in enumerate(mezery2):
        if m >= n:
            idx = sum(cisla2[:(i+1)])
            if i > 0:
                idx += sum(mezery2[:i])
            idx2 = sum(cisla2[:j]) + sum(mezery2[:j])
            if idx >= idx2:
                break
            # print('\t', idx)

            # print('\t', idx)
            disk[idx:idx+n] = [j]*n

            # print('\t idx2=', idx2)
            disk[idx2:idx2+n] = ['.']*n
            # print(mezery2, cisla2)
            # print(disk)
            mezery2[i] -= n
            cisla2[i] += n
            break
print(disk)
res = 0
for i, z in enumerate(disk):
    if z == '.':
        continue
    res += i*int(z)
    # print(i, z)
print(res)
