#D
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = []
for i in range(m):
    b, c = map(int, input().split())
    d.append([b, c])
print(d)
d = sorted(d, key=lambda x: x[1], reverse=True)
print(d)
k = 0
for i in range(n):
    if d[k][0] == 0:#追加できなくなる
        k += 1
        if k == len(d):  #配列末
            break
    if a[i] >= d[k][1]:  #a>=cなのでこれ以上置き換わっても意味がない
        break
    a[i] = d[k][1]  #cに置き換わった
    d[k][0] -= 1  #dの追加出来る数を１減らす
print(sum(a))