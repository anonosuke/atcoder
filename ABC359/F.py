def solve(n, A):
    from heapq import heappop, heappush
    # Sort A in ascending order
    A.sort()
    
    # Initial degrees array with 1 for all except the root node
    degrees = [1] * n
    degrees[0] = 0  # The root node will have degree 0 initially

    # Min-heap to maintain the least degree nodes
    heap = []
    for i in range(n):
        heappush(heap, (degrees[i], i))

    total_cost = 0
    while len(heap) > 1:
        d1, i1 = heappop(heap)
        d2, i2 = heappop(heap)
        
        total_cost += (d1 + 1) ** 2 * A[i2]
        degrees[i2] = d1 + 1
        heappush(heap, (degrees[i2], i2))
    
    # Final cost for the root node
    total_cost += degrees[0] ** 2 * A[0]
    
    print(total_cost)

# Example usage
n = int(input())
A = list(map(int, input().split()))
solve(n, A)
