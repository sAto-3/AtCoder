#C
n = int(input())
a = list(map(int, input().split()))
aa = [[i, a[i]] for i in range(n)]
# print(aa)
aa.sort(key=lambda x: x[1])
# print(aa)
for i in range(n):
    print(aa[i][0] + 1, end=" ")
    