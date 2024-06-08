A, M, L, R = map(int, input().split())

fixL  = L - A
fixR  = R - A

if fixL == fixR:
    print("0")
elif fixL > 0 and fixR > 0:
    if fixL % M == 0 and fixR % M == 0:
        print(fixR//M - fixL//M + 1)
    else:
        print(fixR//M - fixL//M)
elif fixL < 0 and fixR < 0:
    if abs(fixL) % M == 0 and abs(fixR) % M == 0:
        print(abs(fixL)//M - abs(fixR)//M + 1)
    else:
        print(abs(fixL)//M - abs(fixR)//M)
else:
    print((abs(fixR//M) + abs(fixL//M)) + 1)