#D
import math
import numpy as np
n = int(input())
num = np.zeros((10, 10))
for i in range(1, n + 1):
    a = i // pow(10, (int(math.log10(i))))
    b = i % 10
    num[b][a] += 1
ans=0
for i in range(10):
    for j in range(10):
        ans += num[i][j] * num[j][i]
print(int(ans))