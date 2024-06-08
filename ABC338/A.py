S = input()
if S[0].isupper() and (S[1:].islower() or len(S) == 1):
  print("Yes")
else:
  print("No")