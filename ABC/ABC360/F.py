def max_intersecting_segment(n, segments):
    events = []
    for l, r in segments:
        events.append((l, 1))
        events.append((r + 1, -1))
    
    events.sort()
    
    max_intersect = 0
    current_intersect = 0
    best_l = 0
    best_r = 0
    
    for i in range(len(events) - 1):
        current_intersect += events[i][1]
        if current_intersect > max_intersect:
            max_intersect = current_intersect
            best_l = events[i][0]
            best_r = events[i + 1][0] - 1
    
    return best_l, best_r

# 入力の読み込み
n = int(input())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# 答えを計算して出力
l, r = max_intersecting_segment(n, segments)
print(l, r)
