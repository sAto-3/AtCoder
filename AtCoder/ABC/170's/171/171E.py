# E
# ^ : XOR演算子
n = int(input())
a = list(map(int, input().split()))
ans=a[0]
#S=allxor(a)を求める
for i in range(1,n):
    ans = ans ^ a[i]
# print(ans)
b = []
for i in range(n):
    b.append(ans ^ a[i])
print(*b)