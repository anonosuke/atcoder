import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()

min_total_cost = float('inf')
found = False

for combo in itertools.combinations(range(N), M):
    selected_boxes = [(A[i], A[i]) for i in combo]
    selected_boxes.sort(key=lambda x: x[1])
    
    valid = True
    total_cost = 0
    for i in range(M):
        price, sweets = selected_boxes[i]
        if sweets < B[i]:
            valid = False
            break
        total_cost += price
    
    if valid:
        found = True
        min_total_cost = min(min_total_cost, total_cost)

if found:
    print(min_total_cost)
else:
    print(-1)
