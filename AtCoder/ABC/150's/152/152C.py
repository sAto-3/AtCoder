#C
n = int(input())
p = list(map(int, input().split()))
n = p[0]
ans = 1
for i, z in enumerate(p):
    if i == 0:
        continue
    if z <= n:
        ans += 1
    n = min(n, z)
print(ans)