#C
import math
a, b, h, m = map(int, input().split())

def yo(a, b, c):
    #辺a,b 角c
    # print(pow(a, 2), pow(b, 2), 2 * a * b * math.cos(c))
    tmp = pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(c)
    return pow(tmp, 0.5)
ss = (h / 12 + m / 720) * 2 * math.pi
ls = m / 60 * 2 * math.pi
# print(ss, ls, min(abs(ls - ss), 2*math.pi - abs(ls - ss)))
ans = yo(a, b, min(abs(ls - ss), 2*math.pi - abs(ls - ss)))
print(ans)
