S = input()
hash = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

for i in range(len(S)):
  hash[S[i]] += 1

max_value = max(hash.values())
max_key = min([key for key, value in hash.items() if value == max_value])
print(max_key)
