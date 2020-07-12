#C
import math
n, k = map(int, input().split())#n面ダイス 点数k以上
ans = 0
for i in range(1, n + 1):  #出目がi
    if i < k: #出目がk以下
        m = math.ceil(math.log2(k / i))
        ans += 1 / (2 ** m) / n
    else: #出目がk以上
        ans += 1 / n
print(ans)