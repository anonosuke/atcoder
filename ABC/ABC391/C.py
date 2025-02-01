n, q = map(int, input().split())
nest_count = [1] * (n + 1)
pigeon_pos = list(range(n + 1))
over_1 = 0

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, h = query[1], query[2]
        old = pigeon_pos[p]
        nest_count[old] -= 1
        if nest_count[old] == 1:
            over_1 -= 1
        nest_count[h] += 1
        if nest_count[h] == 2:
            over_1 += 1
        pigeon_pos[p] = h
    else:
        print(over_1)
