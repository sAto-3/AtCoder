#B
n=int(input())
a = list(map(int, input().split()))
a.sort()
ans=1
for i in a:
    ans *= i
    if ans == 0:
        break
    if ans > 10 ** 18:
        ans = -1
        break
print(ans)