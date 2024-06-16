# 入力を一行ずつ取得
N = int(input())
heights = []
for _ in range(N):
    heights.append(list(map(int, input().split())))

# 結果を格納するリスト
operations = []

# ダンプカーの状態
dumpcar = 0  # ダンプカーに積んでいる土の量

# 0にならなかったマスを記憶するリスト
not_zero = []

# ループを回して各マスに対して操作を行う
for i in range(N):
    if i % 2 == 0:
        range_j = range(N)
    else:
        range_j = range(N-1, -1, -1)

    for j in range_j:
        current_height = heights[i][j]

        # 土を積む or 降ろす操作
        if current_height > 0:
            operations.append(f"+{current_height}")
            dumpcar += current_height
            heights[i][j] = 0
        elif current_height < 0:
            if dumpcar >= -current_height:
                operations.append(f"-{-current_height}")
                dumpcar += current_height
                heights[i][j] = 0
            elif dumpcar > 0:
                operations.append(f"-{dumpcar}")
                heights[i][j] += dumpcar
                dumpcar = 0
                not_zero.append([i,j])  # 高さを0にできなかったマスを記録
            elif dumpcar == 0:
                not_zero.append([i,j])

        # 移動操作
        if j < N - 1 and i % 2 == 0:
            operations.append("R")
        elif j > 0 and i % 2 == 1:
            operations.append("L")

    if i < N - 1:
        operations.append("D")

# 最後のposition
current_position = [19, 0]

# 未処理のマスに戻って高さを0にする
for x, y in reversed(not_zero):
    if current_position[0] > x:
        while current_position[0] > x:
            operations.append("U")
            current_position[0] -= 1
    elif current_position[0] < x:
        while current_position[0] < x:
            operations.append("D")
            current_position[0] += 1
    
    if current_position[1] > y:
        while current_position[1] > y:
            operations.append("L")
            current_position[1] -= 1
    elif current_position[1] < y:
        while current_position[1] < y:
            operations.append("R")
            current_position[1] += 1

    operations.append(f"{heights[x][y]}")

# 出力
T = len(operations)
for op in operations:
    print(op)
