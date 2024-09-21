M = int(input())

a = [3 ** i for i in range(10, -1, -1)]
b = [i for i in range(10, -1, -1)]

N = 0
result = []
for c, exp in zip(a, b):
    while M >= c and N < 20:
        M -= c
        result.append(exp)
        N += 1

print(N)
print(' '.join(map(str, result)))
