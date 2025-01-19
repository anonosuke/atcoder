import sys
from collections import defaultdict, deque

def read_input():
    N, M, H = map(int, input().split())
    A = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    coords = []
    for _ in range(N):
        x, y = map(int, input().split())
        coords.append((x, y))
    return N, M, H, A, edges, coords

def build_graph(N, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def create_tree(start, graph, N, H, used):
    parents = [-1] * N
    heights = [0] * N
    queue = deque([(start, 0)])
    tree_nodes = {start}
    
    while queue:
        v, h = queue.popleft()
        if h >= H:
            continue
            
        for u in graph[v]:
            if u not in used and u not in tree_nodes:
                parents[u] = v
                heights[u] = h + 1
                tree_nodes.add(u)
                queue.append((u, h + 1))
    
    return parents, tree_nodes

def solve(N, M, H, A, edges, coords):
    graph = build_graph(N, edges)
    used = set()
    final_parents = [-1] * N
    
    # 美しさでソートした頂点リスト
    vertices = sorted(range(N), key=lambda x: A[x], reverse=True)
    
    for start in vertices:
        if start in used:
            continue
            
        parents, tree_nodes = create_tree(start, graph, N, H, used)
        
        # 木に含まれる頂点を使用済みとしてマーク
        used.update(tree_nodes)
        
        # この木の親情報を最終結果に反映
        for v in tree_nodes:
            final_parents[v] = parents[v]
    
    return final_parents

def main():
    N, M, H, A, edges, coords = read_input()
    result = solve(N, M, H, A, edges, coords)
    print(*result)

if __name__ == "__main__":
    main()
