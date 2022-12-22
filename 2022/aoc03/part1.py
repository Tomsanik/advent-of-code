items = {chr(i):(i-96) for i in range(97, 97+26, 1)} | {chr(i):(i-64+26) for i in range(65, 65+26, 1)}

with open('test.txt') as f:
  lines = f.readlines()

score = 0
for l in lines:
  d = len(l)
  c1, c2 = l[:d//2], l[d//2:]
  used = []
  for c in c1:
    if c in c2 and not c in used:
      used.append(c)
      score += items[c]
    
print(score)