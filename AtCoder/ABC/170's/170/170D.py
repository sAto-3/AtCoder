# D
n = int(input())
a = list(map(int, input().split()))
a.sort()
max_a = max(a)
ans = [1 for _ in range(max_a + 1)]
b = -1#存在しない数
#エラトステネスの篩･･･有名な素数判別法

# 1  2  3  4  5  6  7  8  9 
# 11 12 13 14 15 16 17 18 19
#    ×　   ×  ×  ×     ×
#             :

for j in a:
    if b == j:  #行ったところはもう行かない
        ans[j] = 0
    divided = j + j
    while divided < max_a + 1:#jの倍数を0として記録する
        ans[divided] = 0
        divided += j
    b = j

count = 0
for i in a:
    if ans[i] == 1:
        count += 1
print(count)