#B
n = int(input())
w = list(map(int, input().split()))
ans=100
for i in range(n - 1):
    left = sum(w[:i + 1])
    right = sum(w[i + 1:])
    if abs(left - right) < ans:
        ans = abs(left - right)
print(ans)