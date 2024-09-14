def main():
    # すべての入力を読み込む
    N_and_rest = []
    while True:
        try:
            N_and_rest += input().split()
        except EOFError:
            break

    idx = 0
    N = int(N_and_rest[idx])
    idx += 1
    while len(N_and_rest) < idx + N:
        N_and_rest += input().split()
    X = list(map(int, N_and_rest[idx:idx+N]))
    idx += N

    while len(N_and_rest) < idx + 1:
        N_and_rest += input().split()
    Q = int(N_and_rest[idx])
    idx += 1

    T_list = []
    G_list = []
    for _ in range(Q):
        while len(N_and_rest) < idx + 2:
            N_and_rest += input().split()
        T_i = int(N_and_rest[idx]) - 1  # 0-based index
        G_i = int(N_and_rest[idx + 1])
        T_list.append(T_i)
        G_list.append(G_i)
        idx += 2

    N = len(X)
    # 各高橋くんの希望位置と固定フラグを格納
    desired_positions = []
    fixed = [False] * N  # 用事があるかどうか
    for T_i, G_i in zip(T_list, G_list):
        fixed[T_i] = True
        desired_positions.append((G_i, T_i, True, X[T_i]))
    for i in range(N):
        if not fixed[i]:
            desired_positions.append((X[i], i, False, X[i]))

    # 希望位置を大きい順にソート
    desired_positions.sort(reverse=True)

    assigned_positions = [0] * N
    next_available_position = float('inf')
    total_movement = 0

    for pos, idx, is_fixed, init_pos in desired_positions:
        if is_fixed:
            assigned_positions[idx] = pos
            total_movement += abs(pos - init_pos)
            next_available_position = min(next_available_position - 1, pos - 1)
        else:
            assigned_pos = min(pos, next_available_position - 1)
            assigned_positions[idx] = assigned_pos
            total_movement += abs(assigned_pos - init_pos)
            next_available_position = assigned_pos

    print(total_movement)

main()
