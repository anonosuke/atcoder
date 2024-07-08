from collections import deque

def solve(N, S, T):
    # 初期状態と目標状態を作成
    initial_state = [0] * (N + 2)
    target_state = [0] * (N + 2)
    for i in range(N):
        initial_state[i] = 1 if S[i] == 'w' else 2
        target_state[i] = 1 if T[i] == 'w' else 2
    
    # BFSのためのキューと訪問済み状態セット
    queue = deque([(initial_state, 0)])  # (状態, 操作回数)
    visited = set([tuple(initial_state)])
    
    while queue:
        state, moves = queue.popleft()
        
        if state[:N] == target_state[:N]:
            return moves
        
        # 可能な操作をすべて試す
        for i in range(N + 1):
            if state[i] and state[i+1]:
                new_state = state[:]
                new_state[i], new_state[i+1] = 0, 0
                new_state[i-1], new_state[i-2] = state[i], state[i+1]
                
                new_state_tuple = tuple(new_state)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    queue.append((new_state, moves + 1))
    
    return -1  # 目標状態に到達できない場合

# 入力を受け取る
N = int(input())
S = input()
T = input()

# 結果を出力
print(solve(N, S, T))