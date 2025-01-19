import sys
import random
import math
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

def calculate_score(parents, A, N, H):
    score = 1  # ベーススコア
    heights = [0] * N
    for v in range(N):
        curr = v
        height = 0
        while parents[curr] != -1:
            height += 1
            curr = parents[curr]
        heights[v] = height
        score += (height + 1) * A[v]
    return score

def get_tree_nodes(parents, root):
    nodes = {root}
    N = len(parents)
    for v in range(N):
        if parents[v] != -1:
            curr = v
            while curr != -1:
                nodes.add(curr)
                curr = parents[curr]
    return nodes

def is_valid_height(parents, v, H):
    height = 0
    curr = v
    while parents[curr] != -1:
        height += 1
        if height > H:
            return False
        curr = parents[curr]
    return True

def simulated_annealing(N, M, H, A, graph, initial_parents):
    current_parents = initial_parents[:]
    best_parents = initial_parents[:]
    current_score = calculate_score(current_parents, A, N, H)
    best_score = current_score

    # 焼きなましパラメータ
    T_start = 2000.0
    T_end = 1.0
    iterations = 200000
    T = T_start
    cooling_rate = pow(T_end / T_start, 1.0 / iterations)

    for iter in range(iterations):
        # 近傍操作の選択
        operation = random.choice(['change_root', 'change_parent', 'move_subtree'])
        new_parents = current_parents[:]

        if operation == 'change_root':
            # 木の根を変更
            root = random.randint(0, N-1)
            if new_parents[root] != -1:
                old_parent = new_parents[root]
                new_parents[root] = -1
                new_parents[old_parent] = root

        elif operation == 'change_parent':
            # 頂点の親を変更
            v = random.randint(0, N-1)
            if v != -1 and new_parents[v] != -1:
                candidates = list(graph[v])
                if candidates:
                    new_parent = random.choice(candidates)
                    if not creates_cycle(new_parents, v, new_parent):
                        new_parents[v] = new_parent

        else:  # move_subtree
            # 部分木を移動
            v = random.randint(0, N-1)
            if new_parents[v] != -1:
                subtree = get_subtree(new_parents, v)
                new_root = random.choice(list(graph[v]))
                if not any(u == new_root for u in subtree):
                    new_parents[v] = new_root

        # 高さ制限チェック
        valid = all(is_valid_height(new_parents, v, H) for v in range(N))
        if not valid:
            continue

        # スコア計算
        new_score = calculate_score(new_parents, A, N, H)
        delta = new_score - current_score

        # 解の採用判定
        if delta > 0 or random.random() < math.exp(delta / T):
            current_parents = new_parents
            current_score = new_score
            if current_score > best_score:
                best_score = current_score
                best_parents = current_parents[:]

        T *= cooling_rate

    return best_parents

def creates_cycle(parents, v, new_parent):
    curr = new_parent
    while curr != -1:
        if curr == v:
            return True
        curr = parents[curr]
    return False

def get_subtree(parents, root):
    subtree = {root}
    N = len(parents)
    for v in range(N):
        if parents[v] != -1:
            curr = v
            while curr != -1:
                if curr == root:
                    subtree.add(v)
                    break
                curr = parents[curr]
    return subtree

def solve(N, M, H, A, edges, coords):
    graph = build_graph(N, edges)
    
    # 貪欲法で初期解を生成
    initial_parents = [-1] * N
    used = set()
    vertices = sorted(range(N), key=lambda x: A[x], reverse=True)
    
    for start in vertices:
        if start in used:
            continue
        parents, tree_nodes = create_tree(start, graph, N, H, used)
        used.update(tree_nodes)
        for v in tree_nodes:
            initial_parents[v] = parents[v]
    
    # 焼きなまし法で解を改善
    final_parents = simulated_annealing(N, M, H, A, graph, initial_parents)
    return final_parents

def main():
    N, M, H, A, edges, coords = read_input()
    result = solve(N, M, H, A, edges, coords)
    print(*result)

if __name__ == "__main__":
    main()
