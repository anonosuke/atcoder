N = int(input())

size = 3**N
carpet = [["#"] * size for _ in range(size)]

step = 1
while step < size:
    for i in range(size):
        for j in range(size):
            if (i // step) % 3 == 1 and (j // step) % 3 == 1:
                carpet[i][j] = "."
    step *= 3

for row in carpet:
    print("".join(row))
