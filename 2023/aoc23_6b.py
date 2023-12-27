from math import sqrt

with open('aoc23_6a_input.txt') as f:
    data = f.readlines()

data2 = []
for d in data:
    if '\n' in d:
        d = d[:-1]
    while d.find('  ') >= 0:
        d = d.replace('  ', ' ')
    f = d.find(': ')
    x = d[f+2:].replace(' ', '')
    x = int(x)
    data2.append(x)

races = data2
print(races)

t, dr = races
t1 = (t+sqrt(t*t-4*dr))/2
t2 = int((t-sqrt(t*t-4*dr))/2)
n = 1
while t2+n < t1:
    n += 1
n -= 1

print(n)

