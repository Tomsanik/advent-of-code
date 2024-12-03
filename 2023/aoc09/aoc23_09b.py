with open('input.txt') as f:
    data = f.readlines()

res = 0
for d in data:
    if '\n' in d:
        d = d[:-1]
    seq0 = [int(i) for i in d.split(' ')]
    seqs = [seq0]
    end = False
    while not end:
        end = True
        sq = []
        for i in range(len(seqs[0])-1):
            k = seqs[0][i+1]-seqs[0][i]
            sq.append(k)
            if k != 0:
                end = False
        seqs = [sq] + seqs
    print(seqs)

    n = 0
    for s in seqs[1:]:
        n = s[0] - n
    res += n

print(res)
