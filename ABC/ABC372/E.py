N, Q = map(int, input().split())

parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
topk = [[i] for i in range(N + 1)]

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
        topk[v_root] = sorted(topk[v_root] + topk[u_root], reverse=True)[:10]
    else:
        parent[v_root] = u_root
        topk[u_root] = sorted(topk[u_root] + topk[v_root], reverse=True)[:10]
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        _, u, v = query
        u = int(u)
        v = int(v)
        union(u, v)
    else:
        _, v, k = query
        v = int(v)
        k = int(k)
        v_root = find(v)
        if len(topk[v_root]) >= k:
            print(topk[v_root][k - 1])
        else:
            print(-1)
