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

    # 中心の2x2グリッドに値を入れる
    idx = 0
    for i in range(2, 4):
        for j in range(2, 4):
            A[i][j] = sorted_indices[idx]
            idx += 1

    # 次に中心の4x4グリッドに値を入れる
    for i in range(1, 5):
        for j in range(1, 5):
            if A[i][j] == 0:
                A[i][j] = sorted_indices[idx]
                idx += 1

    # 最後に全体の6x6グリッドに値を入れる
    for i in range(6):
        for j in range(6):
            if A[i][j] == 0:
                A[i][j] = sorted_indices[idx]
                idx += 1

    for i in range(N):
        print(' '.join(map(str, A[i])), flush=True)

    X = []

    for i in range(SEED_COUNT):
        X.append(list(map(int, input().split())))
