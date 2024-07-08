def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    edges = []

    for i in range(1, len(data), 3):
        A = int(data[i])
        B = int(data[i+1])
        C = int(data[i+2])
        edges.append(C)

    total_distance = sum(edges)
    print(total_distance)

if __name__ == "__main__":
    main()
