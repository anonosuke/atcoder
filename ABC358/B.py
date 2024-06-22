def ticket_purchase_times(A, N, T):
    purchase_times = [0] * N
    current_time = 0
    for i in range(N):
        arrival_time = T[i]
        if arrival_time > current_time:
            current_time = arrival_time
        purchase_times[i] = current_time + A
        current_time = purchase_times[i]
    return purchase_times

N, A = map(int, input().split())
T = list(map(int, input().split()))

result = ticket_purchase_times(A, N, T)
for time in result:
    print(time)
