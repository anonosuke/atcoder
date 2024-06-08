N = int(input())
X_total = 0
Y_total = 0
for i in range(N):
  X, Y = map(int, input().split())
  X_total += X
  Y_total += Y

if X_total > Y_total:
  print("Takahashi")
elif X_total < Y_total:
  print("Aoki")
else:
  print("Draw")