N, M = map(int, input().split())
H = list(map(int, input().split()))

remaining_sanitizer = M
count = 0

for i in range(N):
    if remaining_sanitizer >= H[i]:
        remaining_sanitizer -= H[i]
        count += 1
    else:
        break

print(count)
