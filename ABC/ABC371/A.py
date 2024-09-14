S_AB, S_AC, S_BC = input().split()

from itertools import permutations

persons = ['A', 'B', 'C']

for perm in permutations(persons):
    age_order = {perm[0]: 0, perm[1]: 1, perm[2]: 2}

    valid = True
    if S_AB == '<':
        if not age_order['A'] < age_order['B']:
            valid = False
    else:
        if not age_order['A'] > age_order['B']:
            valid = False

    if S_AC == '<':
        if not age_order['A'] < age_order['C']:
            valid = False
    else:
        if not age_order['A'] > age_order['C']:
            valid = False

    if S_BC == '<':
        if not age_order['B'] < age_order['C']:
            valid = False
    else:
        if not age_order['B'] > age_order['C']:
            valid = False

    if valid:
        print(perm[1])
        break
