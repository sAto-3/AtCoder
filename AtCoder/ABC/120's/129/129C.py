#C
n, m = map(int, input().split())
a = [1] * (n + 1)#進めるかどうか
b = [1] * (n + 1)#移動方法
#進めない:0 進める:1
for i in range(m):a[int(input())] = 0
mod = 1e9+7
# print(a)
if a[1] == 0:b[1] = 0
for i in range(2, n+1):b[i] = (b[i - 1] + b[i - 2]) * a[i] % mod
    #b[i]=(b[2段前]+b[1段前])*a[i] 進めるかどうか(1,0)
print(int(b[n]))
