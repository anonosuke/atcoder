# 入力を受け取る
N = int(input("行数を入力してください: "))
X = []

for _ in range(N):
    X.append(list(map(int, input().split())))

# 各行の合計値を計算し、合計値と行番号をペアにしてリストにする
sums_with_indices = [(sum(row), index) for index, row in enumerate(X)]

# 合計値で降順にソートする
sums_with_indices.sort(reverse=True, key=lambda x: x[0])

# 結果の行番号を配列に格納する
sorted_indices = [index for _, index in sums_with_indices]

# 結果を出力する
print(sorted_indices)
