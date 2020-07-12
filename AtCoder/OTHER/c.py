import math
n = int(input())
ans = [0] * (n + 1)
for x in range(1, int(math.sqrt(n))):
    for y in range(1, int(math.sqrt(n))):
        for z in range(1, int(math.sqrt(n))):
            a = x * x + y * y + z * z + x * y + y * z + z * x
            if n >= a >= 1:
                ans[a] += 1
print(*ans[1:],sep="\n")