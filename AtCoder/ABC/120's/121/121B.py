#B
n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
# print(a, b)
count=0
for i in a:
    for j in range(len(i)):
        i[j] *= b[j]
    if sum(i) > -c:
        count += 1

print(count)