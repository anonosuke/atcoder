def calculate_toll_fee(Sx, Sy, Tx, Ty):
    # Determine the initial and target tile positions
    initial_tile = (Sx // 2, Sy // 2)
    target_tile = (Tx // 2, Ty // 2)
    
    # Use a set to keep track of visited tiles to avoid recalculating
    visited = set()
    queue = [(initial_tile, 0)]  # (current_tile, toll_fee)
    
    while queue:
        (current_tile, toll_fee) = queue.pop(0)
        
        if current_tile in visited:
            continue
        visited.add(current_tile)
        
        if current_tile == target_tile:
            return toll_fee
        
        # Determine the possible moves (up, down, left, right)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for move in moves:
            next_tile = (current_tile[0] + move[0], current_tile[1] + move[1])
            if next_tile not in visited:
                queue.append((next_tile, toll_fee + 1))
    
    return -1  # In case the target is not reachable

# Example input
Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# Calculate the toll fee
toll_fee = calculate_toll_fee(Sx, Sy, Tx, Ty)
print(toll_fee)  # Expected output: 0 for the example input
