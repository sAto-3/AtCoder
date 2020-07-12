#C
n = int(input())
x = list(map(int, input().split()))
s = sum(x)
s = s / n
if s * 10 % 10 >= 5:
    s = int(s) + 1
else:
    s = int(s)

ans = 0
for i in x:
    ans += (i - s)** 2
print(ans)