def process(n, ds, i):
    if len(ds) == 1:
        print(f'\t{i} KONEC 1')
        return n == ds[0], []
    d = ds[-1]
    if n % d == 0:
        print(f'\t{i}: {n}/{d} = {n // d}')
        b, ops = process(n // d, ds[:-1], i + 1)
        if b:
            ops.append('*')
            return True, ops
    kk = len(str(d))
    if n % 10**kk == d:
        print(f'\t{i}: {n//(10**kk)}||{d} = {n//(10**kk)}{d}')
        b, ops = process(n//(10**kk), ds[:-1], i + 1)
        if b:
            ops.append('||')
            return True, ops
    print(f'\t{i}: {n}-{d} = {n - d}')
    if n - d < 0:
        return False, []
    b, ops = process(n - d, ds[:-1], i)
    if b:
        ops.append('+')
        return True, ops
    else:
        return False, []


ns = []
qs = []
with open('input.txt') as f:
    for i, line in enumerate(f):
        line = line.strip('\n').split(' ')
        ns.append(int(line[0][:-1]))
        qs.append([int(i) for i in line[1:]])

res = 0
for n, qq in zip(ns, qs):
    print(f'Procesuji číslo {n}')
    print(f'\tData: {qq}')
    bol, ops = process(n, qq, 0)
    if bol:
        # print(f'\t {n} OK')
        s = str(qq[0])
        op = ops[0]
        for i in range(1, len(qq)):
            ds = ops[i-1] + str(qq[i])
            if ops[i-1] == '*' and op == '+':
                ds = ')'+ds
                s = '('+s
            op = ops[i-1] if ops[i-1] != '||' else op
            s += ds
        print(f'\t{n}={s}')
        res += n
    # if '||' in ops:
    #     print(ops, qq)
    #     input()
print(res)
