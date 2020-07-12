# 1円5円10円50円100円500円を用いて出来るだけ少ない枚数でA円を支払いたい
# 何枚支払う？

#貪欲法　その場での最善策を探す方法

l = list(map(int, input().split()))
used = l[:6]
a = l[6]
coin = [1, 5, 10, 50, 100, 500]
coin.reverse()
used.reverse()
ans = 0
for i in range(6):
    t = min(a // coin[i], used[i])
    a -= t * coin[i]
    ans += t
    print(coin[i],t)
print(ans)
