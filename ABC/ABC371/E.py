N_and_rest = input().split()
while len(N_and_rest) < 1:
    N_and_rest += input().split()
N = int(N_and_rest[0])
if len(N_and_rest) < N + 1:
    A = N_and_rest[1:] + input().split()
    while len(A) < N:
        A += input().split()
else:
    A = N_and_rest[1:]

A = list(map(int, A))

N = len(A)
prev = {}
total_sum = 0

for i in range(1, N + 1):
    val = A[i - 1]
    previous_occurrence = prev.get(val, 0)
    contribution = (i - previous_occurrence) * (N - i + 1)
    total_sum += contribution
    prev[val] = i

print(total_sum)
