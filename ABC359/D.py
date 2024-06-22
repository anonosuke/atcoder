MOD = 998244353

def is_good_string(s, K):
    n = len(s)
    for i in range(n - K + 1):
        sub = s[i:i + K]
        if sub == sub[::-1]:
            return False
    return True

def count_good_strings(S, K):
    n = len(S)
    count = 0

    def backtrack(index, current):
        nonlocal count
        if index == n:
            if is_good_string(current, K):
                count += 1
                count %= MOD
            return
        if S[index] == '?':
            backtrack(index + 1, current + 'A')
            backtrack(index + 1, current + 'B')
        else:
            backtrack(index + 1, current + S[index])

    backtrack(0, '')
    return count

N, K = map(int, input().split())
S = input().strip()

result = count_good_strings(S, K)
print(result)
