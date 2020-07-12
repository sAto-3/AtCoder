#B
import math
n, k = map(int, input().split())
i=0
while True:
    tmp=k**i
    if tmp > n:
        break
    i += 1
print(i)