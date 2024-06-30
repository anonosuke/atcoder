def hungarian_algorithm(cost_matrix):
    n = len(cost_matrix)
    u = [0] * n
    v = [0] * n
    p = [-1] * n
    way = [0] * n

    for i in range(n):
        p[0] = i
        j0 = 0
        minv = [float('inf')] * n
        used = [False] * n
        while p[j0] != -1:
            used[j0] = True
            i0 = p[j0]
            delta = float('inf')
            j1 = 0
            for j in range(n):
                if not used[j]:
                    cur = cost_matrix[i0][j] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(n):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
        while j0 != 0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    return [-p[j] for j in range(n)]

def solve(N, A, W):
    cost_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[i] != j + 1:
                cost_matrix[i][j] = W[i]

    matching = hungarian_algorithm(cost_matrix)
    total_cost = sum(cost_matrix[i][matching[i]] for i in range(N))
    return total_cost

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

result = solve(N, A, W)
print(result)