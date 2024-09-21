N = int(input())
H = list(map(int, input().split()))
res = [0] * N
S = []

for i in range(N-1, -1, -1):
    count = 0
    while S and H[S[-1]] < H[i]:
        S.pop()
        count += 1
    res[i] = count + len(S)
    S.append(i)

print(' '.join(map(str, res)))
