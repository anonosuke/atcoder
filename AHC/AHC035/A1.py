N, M, T = map(int, input().split())
SEED_COUNT = 2 * N * (N - 1)
X = []

for i in range(SEED_COUNT):
    X.append(list(map(int, input().split())))

for t in range(T):
    # 種子の評価項目の最大値を求め、最大のもののみ使用するようにする
    # 各行の合計値を計算し、合計値と行番号をペアにしてリストにする
    sums_with_indices = [(sum(row), index) for index, row in enumerate(X)]
    # 合計値で降順にソートする
    sums_with_indices.sort(reverse=True, key=lambda x: x[0])
    # 結果の行番号を配列に格納する
    sorted_indices = [index for _, index in sums_with_indices]

    A = [[0] * N for i in range(N)]

    # ここの処理を作る
    for i in range(N):
        for j in range(N):
            A[i][j] = sorted_indices[i * N + j]

    for i in range(N):
        print(' '.join(map(str, A[i])), flush=True)

    X = []

    for i in range(SEED_COUNT):
        X.append(list(map(int, input().split())))