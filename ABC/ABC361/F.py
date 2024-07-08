def count_power_representations(N):
    seen = set()
    for b in range(2, 60):  # log2(10^18) ≈ 59.79
        a = 2
        while True:
            power = pow(a, b)
            if power > N:
                break
            if power not in seen:
                seen.add(power)
            a += 1
    return len(seen)

# 入力を受け取る
N = int(input())

# 結果を計算して出力
result = count_power_representations(N)
print(result + 1)