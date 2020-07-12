#D
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = [a[0]]
for i in range(1, n - n // 2 + 1):
    ans.append(a[i])
    ans.append(a[i])
print(sum(ans[:n - 1]))