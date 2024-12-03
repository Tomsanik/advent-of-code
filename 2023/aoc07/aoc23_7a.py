with open('input.txt') as f:
    data = f.readlines()

cards0 = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0}
c_s = 'AKQJT98765432'

def value(a: str) -> (int, dict):
    cards = cards0.copy()
    for c in a:
        cards[c] += 1
    vals = list(cards.values())
    vals.sort(reverse=True)
    if vals[0] == 5:
        val = 6
    elif vals[0] == 4:
        val = 5
    elif vals[0] == 3:
        if vals[1] == 2:
            val = 4
        else:
            val = 3
    elif vals[0] == 2:
        if vals[1] == 2:
            val = 2
        else:
            val = 1
    else:
        val = 0
    return val, list(cards.values())


def first_higher(a, b) -> bool:
    val_a, c_a = value(a)
    val_b, c_b = value(b)
    if val_a > val_b:
        return True
    elif val_a < val_b:
        return False
    else:
        for x, y in zip(a, b):
            i_x, i_y = c_s.find(x), c_s.find(y)
            if i_x < i_y:
                return True
            elif i_y < i_x:
                return False


hands = []
bids = []
for d in data:
    if '\n' in d:
        d = d[:-1]
    hand, bid = d.split(' ')
    hands.append(hand)
    bids.append(bid)
print(hands)
print(bids)

kont = True
while kont:
    kont = False
    for i in range(len(hands)-1):
        c1, c2 = hands[i], hands[i+1]
        if first_higher(c1, c2):
            p = hands[i]
            hands[i] = hands[i+1]
            hands[i+1] = p
            p = bids[i]
            bids[i] = bids[i + 1]
            bids[i + 1] = p
            kont = True
print(hands)
print(bids)

for i in range(len(bids)):
    bids[i] = int(bids[i])
    bids[i] *= i+1

print(len(bids))
print(sum(bids))
