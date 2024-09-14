N, M = map(int, input().split())

male_child_in_house = [False] * (N + 1)

for _ in range(M):
    Ai, Bi = input().split()
    Ai = int(Ai)
    if Bi == 'M':
        if not male_child_in_house[Ai]:
            print('Yes')
            male_child_in_house[Ai] = True
        else:
            print('No')
    else: 
        print('No')
