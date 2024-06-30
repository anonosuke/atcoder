
N = int(input())

colors = list(map(int, input().split()))

count = 0

for i in range(2 * N):
    for j in range(i + 1, 2 * N):
        if colors[i] == colors[j] and abs(i - j) == 2:
            count += 1

print(count)