#B
a, b, c, k = map(int, input().split())
ans=0
if a < k:
    ans += 1 * a
    k -= a
    if b < k:
        k -= b
        if c < k:
            ans += -1 * (c - k)
        else:
            ans += -1 * k
else:
    ans+=1*k
print(ans)
