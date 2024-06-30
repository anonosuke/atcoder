N = int(input())
a = list(map(int, input().split()))

# グラフの隣接リスト
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i].append(a[i] - 1)  # 頂点は1から始まるので、0始まりに変換

# 深さ優先探索を用いて強連結成分を求める
def dfs(v, visited, stack, graph):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, graph)
    stack.append(v)

def reverse_graph(graph):
    N = len(graph)
    reversed_graph = [[] for _ in range(N)]
    for v in range(N):
        for neighbor in graph[v]:
            reversed_graph[neighbor].append(v)
    return reversed_graph

def find_sccs(graph):
    N = len(graph)
    visited = [False] * N
    stack = []
    
    # 1回目のDFSで帰りがけ順を記録
    for i in range(N):
        if not visited[i]:
            dfs(i, visited, stack, graph)
    
    reversed_graph = reverse_graph(graph)
    
    # 2回目のDFSで強連結成分を抽出
    visited = [False] * N
    sccs = []
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            component_stack = []
            dfs(v, visited, component_stack, reversed_graph)
            sccs.append(component_stack)
    
    return sccs

sccs = find_sccs(graph)

# 強連結成分ごとに組の数を計算
reachable_pairs = 0
for scc in sccs:
    size = len(scc)
    reachable_pairs += size * size  # 各強連結成分内の頂点の組み合わせ

print(reachable_pairs)
