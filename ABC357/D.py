N = int(input())
mod = 998244353

length = len(str(N))
VN_mod = (N * (pow(10, length * N, mod) - 1) * pow(10**length - 1, -1, mod)) % mod

print(VN_mod)
