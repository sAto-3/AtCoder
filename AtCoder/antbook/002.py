# Ants
l = int(input())
n = int(input())
x = list(map(int, input().split()))
# 最小時間を求める
min_ans = 0
# 最大時間を求める
max_ans = 0
for i in range(n):
    min_ans = max(min_ans, min(l - x[i], x[i]))
    max_ans = max(max_ans, l - x[i], x[i])
print(min_ans)
print(max_ans)
