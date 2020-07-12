#B
a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for i in range(n):
    m = int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k] == m:
                a[j][k] = 0
f = False
for j in range(3):
    if a[j][0] == a[j][1] == a[j][2] == 0 or a[0][j] == a[1][j] ==a[2][j] == 0:
        f = True
if (a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0) or (a[2][0] == 0 and a[1][1] == 0 and a[0][2] == 0):
    f = True
if f:
    print('Yes')
else:
    print('No')