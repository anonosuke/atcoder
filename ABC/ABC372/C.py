N, Q = map(int, input().split())
S = list(input())
count = 0
N = len(S)

def check(i):
    return S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C'

for i in range(N - 2):
    if check(i):
        count += 1

for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1
    for i in range(X - 2, X + 1):
        if 0 <= i <= N - 3:
            if check(i):
                count -= 1
    S[X] = C
    for i in range(X - 2, X + 1):
        if 0 <= i <= N - 3:
            if check(i):
                count += 1
    print(count)
