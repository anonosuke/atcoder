def solve(n, intervals):
    L = [interval[0] for interval in intervals]
    R = [interval[1] for interval in intervals]

    total_L = sum(L)
    total_R = sum(R)

    if total_L > 0 or total_R < 0:
        return "No"

    X = L[:]
    surplus = -total_L

    for i in range(n):
        increase = min(surplus, R[i] - L[i])
        X[i] += increase
        surplus -= increase

        if surplus == 0:
            break

    return "Yes\n" + " ".join(map(str, X))


n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

result = solve(n, intervals)
print(result)
