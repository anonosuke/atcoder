N = int(input())
binary = bin(N)[2:]

count = 0

for i in range(1, len(binary) + 1):
  if binary[-i] == "0":
    count += 1
  else:
    break

print(count)