zapis = open('input.txt').readline().strip()
# print(zapis)

disk = []
i = 0
for z in zapis:
    if i % 2 == 1:
        disk += ['.']*int(z)
    else:
        disk += [str(i//2)]*int(z)
    i += 1
# disk = ''.join(disk)
print(disk)

mezery = [i for i in range(len(disk)) if disk[i] == '.']
# print(mezery)

j = 0
for i in range(len(mezery)):
    while disk[-i-1-j] == '.':
        j += 1
    if mezery[i] >= len(disk)-i-j:
        break
    disk[mezery[i]] = disk[-i-1-j]
    disk[-i-1-j] = '.'
    # print(k)
    # print(''.join(disk))
print(disk)
res = 0
for i, z in enumerate(disk):
    if z == '.':
        break
    res += i*int(z)
    # print(i, z)
print(res)