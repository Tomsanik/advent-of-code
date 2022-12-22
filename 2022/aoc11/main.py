from monkey import Monkey


monkeys = []
monkeys.append(Monkey([74, 73, 57, 77, 74], [False, 11], 19, [6, 7]))

monkeys.append(Monkey([99, 77, 79], [True, 8], 2, [6, 0]))
monkeys.append(Monkey([64, 67, 50, 96, 89, 82, 82], [True, 1], 3, [5, 3]))

monkeys.append(Monkey([88], [False, 7], 17, [5, 4]))
monkeys.append(Monkey([80, 66, 98, 83, 70, 63, 57, 66], [True, 4], 13, [0, 1]))

monkeys.append(Monkey([81, 93, 90, 61, 62, 64], [True, 7], 7, [1, 4]))
monkeys.append(Monkey([69, 97, 88, 93], [False, 0], 5, [7, 2]))

monkeys.append(Monkey([59, 80], [True, 6], 11, [2, 3]))

# monkeys.append(Monkey([79, 98], [False, 19], 23, [2, 3]))
# monkeys.append(Monkey([54, 65, 75, 74], [True, 6], 19, [2, 0]))

# monkeys.append(Monkey([79, 60, 97], [False, 0], 13, [1, 3]))
# monkeys.append(Monkey([74], [True, 3], 17, [0, 1]))


divs = [m.test_div for m in monkeys]
dd = 1
for d in divs:
    dd *= d
print('dd =', dd)
asdasd = [1, 20] + [i*1000 for i in range(1,11, 1)]

N = 10000

for i in range(1, N+1, 1):
    for m in monkeys:
        for it in m.items:
            newit = m.operation(it)
            # newit = newit // 3
            newit = newit % dd
            to = m.test(newit)
            monkeys[to].catch(newit)
        m.throw_out()
    if i in asdasd:
        print('After round', i)
        for j, m in enumerate(monkeys):
            print(f'\tMonkey {j}: \t {m.oper_count}')

counts = []
for m in monkeys:
    counts.append(m.oper_count)
    # print(m.oper_count)

i, j = 0, 0
for k in counts:
    if k > i:
        j = i
        i = k
    elif k > j:
        j = k

print(i, j, i*j)
