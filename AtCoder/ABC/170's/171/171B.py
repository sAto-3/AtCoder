# B
n, k = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
print(p)
print(sum(p[:k]))
