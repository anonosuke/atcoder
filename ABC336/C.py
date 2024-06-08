N = int(input())

N_base_5 = ""
while N > 0:
  N_base_5 = str((N - 1) % 5) + N_base_5
  N = (N - 1) // 5

print(N)
N_base_10 = int(N_base_5) - 1
print(N_base_10)

N_base_10_doubled = int(''.join(str(int(digit) * 2) for digit in str(N_base_10)))
print(N_base_10_doubled)