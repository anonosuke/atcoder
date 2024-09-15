N = int(input())
target_beverages = []
for _ in range(N):
    A, B = map(int, input().split())
    target_beverages.append((A, B))

target_beverages.sort(key=lambda x: x[0] + x[1])

S = [(0, 0)]
operations = []

for A_i, B_i in target_beverages:
    min_cost = None
    min_x = min_y = None

    for x, y in S:
        if x <= A_i and y <= B_i:
            cost = (A_i - x) + (B_i - y)
            if min_cost is None or cost < min_cost:
                min_cost = cost
                min_x, min_y = x, y

    operations.append((min_x, min_y, A_i, B_i))
    S.append((A_i, B_i))

M = len(operations)
print(M)
for op in operations:
    print(f"{op[0]} {op[1]} {op[2]} {op[3]}")
