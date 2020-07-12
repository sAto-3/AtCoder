# B
a, b = map(int, input().split())
aa = str(a) * b
bb = str(b) * a
if a < b:
    print(aa)
else:
    print(bb)
