S = input()

uppercase_count = sum(1 for c in S if c.isupper())
lowercase_count = sum(1 for c in S if c.islower())

if uppercase_count > lowercase_count:
    S = S.upper()
else:
    S = S.lower()

print(S)