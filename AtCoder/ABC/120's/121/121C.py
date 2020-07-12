#C
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
ans = 0
count = 0
for i in range(n):
    if m < ab[i][1]:
        ans += m * ab[i][0]
        break
    ans += ab[i][0] * ab[i][1]
    m -= ab[i][1]
    if count >= m:
        break
print(ans)
