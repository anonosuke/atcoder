N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        match = True
        for k in range(M):
            for l in range(M):
                if S[i+k][j+l] != T[k][l]:
                    match = False
                    break
            if not match:
                break
        if match:
            print(i + 1, j + 1)
            exit()
