#C
n, m = map(int, input().split())
l = []
r = []
for _ in range(m):
    tmp=list(map(int,input().split()))
    l.append(tmp[0])
    r.append(tmp[1])
lmax = max(l)
rmin = min(r)
# print(lmax,rmin)
if rmin >= lmax:
    print(rmin -lmax + 1)
else:
    print(0)
