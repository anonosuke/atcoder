S = input()

if S == "A" or S == "B" or S == "C":
  print("Yes")
else:
  if not S[0] == "A":
    print("No")
    exit()
  else:
      for i in range(len(S)):
        if not S[i] == "A":
          S = S[i:]
          break
      if not S[0] == "B" :
        print("No")
        exit()
      else:
        for i in range(len(S)):
          if not S[i] == "B":
            S = S[i:]
            break
        if not S[0] == "C":
          print("No")
          exit()
        else:
          print("Yes")