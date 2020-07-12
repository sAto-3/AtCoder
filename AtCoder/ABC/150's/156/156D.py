#D
n, a, b = map(int, input().split())
mod = pow(10, 9) + 7


def nCr(n, x):
    numerator = 1
    for i in range(n, n - x, -1):
        numerator = numerator * i % mod

    denominator = 1
    for j in range(x, 1, -1):
        denominator = denominator * j % mod

    d = pow(denominator, mod-2, mod)

    return numerator * d

# #pow
# # def pow(x, n, mod=10e9+7):
# #     ans = 1
# #     while (n > 0):
# #         if bin(n & 1) == bin(1):
# #             ans *= x
# #         x *= x
# #         n = n >> 1
# #     return ans

a = nCr(n, a)
b = nCr(n, b)

print((pow(2, n, mod) - 1 - a - b) % mod)
