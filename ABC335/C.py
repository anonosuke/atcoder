class PointsManager:
    def __init__(self, N):
        self.points = [(i, 0) for i in range(1, N + 1)]
        self.cache = {i: (i, 0) for i in range(1, N + 1)}

    def move(self, direction):
        print(self.cache)
        print(self.points)
        print()
        self.cache[1] = self.points[0]
        print(self.cache)
        print(self.points)

        x, y = self.points[0]
        if direction == 'R':
            self.points[0] = (x + 1, y)
        elif direction == 'L':
            self.points[0] = (x - 1, y)
        elif direction == 'U':
            self.points[0] = (x, y + 1)
        elif direction == 'D':
            self.points[0] = (x, y - 1)

        for i in range(1, len(self.points)):
            self.points[i], self.cache[i + 1] = self.cache[i], self.points[i]

    def get_position(self, index):
        x, y = self.points[index - 1]
        return f"{x} {y}"
    
N, Q = map(int, input().split())
queries = []
for _ in range(Q):
    queries.append(input().split())

manager = PointsManager(N)
for query in queries:
    Q1, Q2 = query
    if Q1 == '1':
        manager.move(Q2)
    elif Q1 == '2':
        print()
        print()
        # print(manager.get_position(int(Q2)))