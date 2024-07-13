import itertools
MOD = 998244353

def is_arithmetic_sequence(seq):
    if len(seq) < 2:
        return True
    d = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] != d:
            return False
    return True

def count_arithmetic_subsequences(arr):
    total_counts = [0] * (N + 1)

    for k in range(1, N + 1):
        count = 0
        combinations = list(itertools.combinations(A, k))
        combinations_2d = [list(combination) for combination in combinations]
        for combination in combinations_2d:
            if is_arithmetic_sequence(combination):
                count += 1
        total_counts[k] = count % MOD

    return total_counts[1:]

N = int(input())
A = list(map(int, input().split()))

result = count_arithmetic_subsequences(A)
print(" ".join(map(str, result)))
