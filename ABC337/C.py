N = int(input())
A = list(map(int, input().split()))

index = A.index(-1)
ex_num = 0
num = []
num.append(index + 1)

for i in range(N):
  index = A.index(index)
  num.append(index + 1)

print(num)