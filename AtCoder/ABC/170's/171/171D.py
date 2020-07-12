# D
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
q = int(input())
bc = [list(map(int, input().split())) for _ in range(q)]
a = Counter(a)
# print(a, sum_a)
for i in range(q):
    # print(a)
    # print(bc[i][0], bc[i][1], sum_a)
    num = a[bc[i][0]]*bc[i][1]
    sum_a = sum_a - (a[bc[i][0]] * bc[i][0]) + num

    a[bc[i][1]] += a[bc[i][0]]
    a[bc[i][0]] = 0
    print(sum_a)
