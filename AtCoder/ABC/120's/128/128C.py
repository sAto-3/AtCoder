#C
n, m = map(int, input().split())
k = [] * m
s = [] * m
p = [] * m
for i in range(m):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    s.append(ks[1:])
p = list(map(int, input().split()))
ans=0
# print(k, s, p)
for i in range(2 ** n):
    on = True
    for j in range(m):
        light = 0
        for k in s[j]:
            tmp = i >> (k-1) & 1
            light = (light + tmp) % 2
        if light != p[j]:
            on = False
            break
    ans += int(on)
print(ans)