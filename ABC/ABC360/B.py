S, T = input().split()

mozi = len(S) // len(T)
amari = len(S) % len(T)
ketu = mozi - amari

hikaku = ''

if len(T) == 1:
    print('No')
    exit()

for i in range(1, ketu + 1):
    for j in range(1,len(T)+1):
        hikaku += S[(j * mozi) - i]
    if hikaku == T:
        print('Yes')
        exit()
    else:
        hikaku = ''

kakuninn = ketu // (len(T) - 1)

next_mozi = 0
next_amari = 0

for i in range(1, kakuninn + 1):
    next_mozi = mozi + i
    next_amari = len(S) % next_mozi
    for j in range(next_amari):
        for k in range(len(T)):
            hikaku += S[(k * next_mozi) + j]
        if hikaku == T:
            print('Yes')
            exit()
        else:
            hikaku = ''

print('No')