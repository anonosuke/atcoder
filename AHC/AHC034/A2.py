import heapq

# 入力を一行ずつ取得
N = int(input())
heights = []
for _ in range(N):
    heights.append(list(map(int, input().split())))

# 結果を格納するリスト
operations = []

# ダンプカーの状態
dumpcar = 0  # ダンプカーに積んでいる土の量
current_position = (0, 0)

def move_and_record(from_pos, to_pos):
    fx, fy = from_pos
    tx, ty = to_pos
    while fx < tx:
        operations.append("D")
        fx += 1
    while fx > tx:
        operations.append("U")
        fx -= 1
    while fy < ty:
        operations.append("R")
        fy += 1
    while fy > ty:
        operations.append("L")
        fy -= 1

# マスの優先度を計算（高さの絶対値が大きいマスを優先）
priority_queue = []
for i in range(N):
    for j in range(N):
        heapq.heappush(priority_queue, (-abs(heights[i][j]), i, j))

while priority_queue:
    _, x, y = heapq.heappop(priority_queue)
    if heights[x][y] == 0:
        continue

    # 移動して操作を記録
    move_and_record(current_position, (x, y))
    current_position = (x, y)
    
    # 土を積む or 降ろす操作
    current_height = heights[x][y]
    if current_height > 0:
        operations.append(f"+{current_height}")
        dumpcar += current_height
        heights[x][y] = 0
    elif current_height < 0:
        if dumpcar >= -current_height:
            operations.append(f"-{-current_height}")
            dumpcar += current_height
            heights[x][y] = 0
        elif dumpcar > 0:
            operations.append(f"-{dumpcar}")
            heights[x][y] += dumpcar
            dumpcar = 0

# 出力
T = len(operations)
for op in operations:
    print(op)
