import bisect

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

prefix_P = [0]
for p in P:
    prefix_P.append(prefix_P[-1] + p)

Q = int(input())
X_list = X

queries = []
input_lines_needed = Q
input_lines_read = 0
while input_lines_read < input_lines_needed:
    line = input().strip()
    if not line:
        continue
    parts = line.split()
    while len(parts) < 2:
        next_line = input().strip()
        if next_line:
            parts.extend(next_line.split())
    L, R = map(int, parts[:2])
    queries.append((L, R))
    input_lines_read += 1

for L, R in queries:
    left = bisect.bisect_left(X_list, L)
    right = bisect.bisect_right(X_list, R)
    total = prefix_P[right] - prefix_P[left]
    print(total)
