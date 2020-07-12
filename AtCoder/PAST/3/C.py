import sys
a, r, n = map(int, input().split())
ans = a
if r == 1 or n == 1:
    pass
else:
    for i in range(n-1):
        ans *= r
        # print(ans)
        if ans > 10e9:
            break
if ans > 10e9:
    print('large')
else:
    print(ans)
