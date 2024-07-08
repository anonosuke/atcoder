N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

min_difference = float('inf')

for i in range(K + 1):
    current_difference = A[i + (N - K) - 1] - A[i]
    min_difference = min(min_difference, current_difference)

print(min_difference)
