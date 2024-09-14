def min_cyclic_shift(arr):
    n = len(arr)
    s = arr + arr
    i, j, k = 0, 1, 0
    while i < n and j < n:
        if s[i + k] == s[j + k]:
            k += 1
            if k == n:
                break
        elif s[i + k] > s[j + k]:
            i += k + 1
            if i == j:
                i += 1
            k = 0
        else:
            j += k +1
            if i == j:
                j += 1
            k = 0
    pos = min(i, j)
    return arr[pos:] + arr[:pos]

def main():
    N = int(input())
    P = list(map(int, input().split()))
    A = list(map(int, input().split()))

    visited = [False] * N
    result = [0] * N

    for i in range(N):
        if not visited[i]:
            cycle = []
            idx = i
            while not visited[idx]:
                visited[idx] = True
                cycle.append(idx)
                idx = P[idx] - 1

            elements = [A[idx] for idx in cycle]
            min_rotation = min_cyclic_shift(elements)

            for idx, val in zip(cycle, min_rotation):
                result[idx] = val

    print(' '.join(map(str, result)))

main()
