with open('aoc23_1a_input.txt') as f:
    input = f.readlines()
aoc23_1.py
nums = [str(i) for i in range(10)]
n = 0
for inp in input:
    k = True
    for c in inp:
        if c in nums:
            m = int(c)
            if k:
                n += 10*m
                k = False
    n += m

print(n)
