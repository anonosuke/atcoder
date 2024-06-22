N = int(input())
H = list(map(int, input().split()))

A = [0] * (N + 1)
result = [0] * N
operation_count = 0

for _ in range(10**9):
    operation_count += 1
    A[0] += 1
    
    for i in range(1, N + 1):
        if A[i-1] > A[i] and A[i-1] > H[i-1]:
            A[i-1] -= 1
            A[i] += 1
            if A[i] == 1:
                result[i-1] = operation_count
    
    if all(r > 0 for r in result):
        break

print(*result)