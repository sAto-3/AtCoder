# B
n, k = map(int, input().split())
d = []
a = []
people = [0] * n
for i in range(k):
    d.append(int(input()))
    a.append(list(map(int, input().split())))
# print(a)
for i in range(k):
    for j in range(d[i]):
        # print(d[i])
        people[a[i][j]-1] += 1
ans = 0
# print(people)
for i in people:
    if i == 0:
        ans += 1
print(ans)
