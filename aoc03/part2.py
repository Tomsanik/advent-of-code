items = {chr(i):(i-96) for i in range(97, 97+26, 1)} | {chr(i):(i-64+26) for i in range(65, 65+26, 1)}

with open('input.txt') as f:
  lines = f.readlines()

score = 0
for i in range(len(lines) // 3):
  group = lines[3*i:3*(i+1)]
  shortest = 0
  for j in range(len(group)):
    group[j] = group[j].strip('\n')
    if len(group[j]) < len(group[shortest]):
      shortest = j
  for c in group[shortest]:
    if c in group[(shortest+1)%3] and c in group[(shortest+2)%3]:
      score += items[c]
      break

    
print(score)