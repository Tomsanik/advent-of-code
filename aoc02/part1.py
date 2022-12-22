with open('input.txt') as f:
  lines = f.readlines()

op = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

score = 0
for l in lines:
  sc = 0
  a, x = l.split()
  i = op.index(a)
  j = me.index(x)
  sc += j+1
  if i == j:
    sc += 3
  elif (i, j) in [(0, 1), (1, 2), (2, 0)]:
    sc += 6
  score += sc

print(score)
    