#B
n = int(input())

sp = [list(input().split()) for i in range(n)]
for i in range(n):
    sp[i].append(i + 1)
# print(sp)
sspp = sorted(sp, key=lambda x: int(x[1]), reverse=True)
sspp.sort(key=lambda x: x[0])
for i in range(n):
    print(sspp[i][2])