N, M, T = map(int, input().split())
SEED_COUNT = 2 * N * (N - 1)
X = []

for i in range(SEED_COUNT):
    X.append(list(map(int, input().split())))

def fill_grid(A, sorted_indices):
    index = 0
    
    def fill_cell(i, j):
        nonlocal index
        if 0 <= i < N and 0 <= j < N and A[i][j] == 0:
            A[i][j] = sorted_indices[index]
            index += 1
    
    for start_row in range(1, N-1):
        for start_col in range(1, N-1):
            fill_cell(start_row, start_col)
            fill_cell(start_row+1, start_col)
            fill_cell(start_row, start_col+1)
            fill_cell(start_row-1, start_col)
            fill_cell(start_row, start_col-1)
    
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                A[i][j] = sorted_indices[index]
                index += 1

for t in range(T):
    sums_with_indices = [(sum(row), index) for index, row in enumerate(X)]
    sums_with_indices.sort(reverse=True, key=lambda x: x[0])
    sorted_indices = [index for _, index in sums_with_indices]

    A = [[0] * N for _ in range(N)]
    
    fill_grid(A, sorted_indices)

    for i in range(N):
        print(' '.join(map(str, A[i])), flush=True)

    X = []

    for i in range(SEED_COUNT):
        X.append(list(map(int, input().split())))
