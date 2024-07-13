R, G, B = map(int, input().split())
C = input().strip()

prices = []

if C != "Red":
    prices.append(R)
if C != "Green":
    prices.append(G)
if C != "Blue":
    prices.append(B)

min_price = min(prices)
print(min_price)
