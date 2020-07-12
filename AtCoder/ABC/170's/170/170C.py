# C
x, n = map(int, input().split())
p = list(map(int, input().split()))
# print(p)
ans = 0
if n == 0:
    print(x)
elif x not in p:
    print(x)
else:
    for i in range(102):
        if i not in p:
            if abs(x - i) < abs(x - ans):
                ans = i
    print(ans)
