def count_crossings(N, T, S, positions):
    ants = sorted((positions[i], S[i]) for i in range(N))
    
    count = 0
    left = []
    
    for pos, direction in ants:
        if direction == '1':
            left.append(pos)
        else:
            count += len([x for x in left if pos - x <= 2 * T])
    
    return count

N, T = map(int, input().split())
S = input().strip()
positions = list(map(int, input().split()))

result = count_crossings(N, T, S, positions)

print(result)
