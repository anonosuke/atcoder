MOD = 998244353

def expected_position(N, K):
    dp = [0] * (N + 1)
    dp[1] = 1  # 黒いボールが最初は一番左にあるので初期値は1

    for _ in range(K):
        new_dp = [0] * (N + 1)
        for i in range(1, N + 1):
            new_dp[i] = (new_dp[i - 1] + dp[i]) * (N - 1) % MOD
        dp = new_dp

    return dp[N]

N, K = map(int, input().split())
print(expected_position(N, K))
