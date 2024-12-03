with open('aoc23_1b_input.txt') as f:
    data = f.readlines()

num_c = [str(i) for i in range(10)]
num_s = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
n = 0
for inp in data:
    if '\n' in inp:
        inp = inp[:-1]
    print(inp)
    r = []
    for i in range(len(inp)):
        for num in num_s+num_c:
            k = inp[i:].find(num)
            if k == 0:
                if num in num_s:
                    cc = int(num_s.index(num)+1)
                else:
                    cc = int(num)
                r.append(cc)
    n += r[0]*10+r[-1]

print(n)

#     r, q = [], []
#     inp2 = inp
#     for c in num_s+num_c:
#         while c in inp2:
#             k = inp.find(c)
#             r.append(k)
#             if c in num_s:
#                 cc = int(num_s.index(c)+1)
#             else:
#                 cc = int(c)
#             q.append(cc)
#             l = inp2.find(c)
#             inp2 = inp2[0:l]+inp2[l+len(c):]
#             # print('\t', c, l, inp2)
#     r = np.array(r)
#     q = np.array(q)
#     idx = np.argsort(r)
#     q = q[idx]
#     r.sort()
#     print('\t', r)
#     print('\t', q)
#     # input.txt()
