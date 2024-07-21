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

    A = [[0] * N for _ in range(N)]

    # 中央部分のN-2 x N-2の部分に右下から左に、次に上の行の右に向かってsorted_indicesの値を入れる
    idx = 0
    for i in range(N-2, 0, -1):
        for j in range(N-2, 0, -1):
            A[i][j] = sorted_indices[idx]
            idx += 1

    # 1行目、N行目、1列目、N列目に残りのsorted_indicesの値を入れる
    for i in range(N):
        if i == 0 or i == N-1:
            for j in range(N):
                if A[i][j] == 0:
                    A[i][j] = sorted_indices[idx]
                    idx += 1
        else:
            if A[i][0] == 0:
                A[i][0] = sorted_indices[idx]
                idx += 1
            if A[i][N-1] == 0:
                A[i][N-1] = sorted_indices[idx]
                idx += 1

    for i in range(N):
        print(' '.join(map(str, A[i])), flush=True)

    X = []

    for i in range(SEED_COUNT):
        X.append(list(map(int, input().split())))
