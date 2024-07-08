def solve(a, b, c, d, e, f, g, h, i, j, k, l):
    
    x_overlap = max(0, min(d, j) - max(a, g))
    y_overlap = max(0, min(e, k) - max(b, h))
    z_overlap = max(0, min(f, l) - max(c, i))
    
    volume_overlap = x_overlap * y_overlap * z_overlap
    
    if volume_overlap > 0:
        print("Yes")
    else:
        print("No")

a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

solve(a, b, c, d, e, f, g, h, i, j, k, l)
