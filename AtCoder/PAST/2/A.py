s, t = map(str, input().split())
l = ["B9", "B8", "B7", "B6", "B5", "B4", "B3", "B2", "B1",
     "1F", "2F", "3F", "4F", "5F", "6F", "7F", "8F", "9F"]
ss = 0
tt = 0
for i in range(len(l)):
    if s == l[i]:
        ss = i
    if t == l[i]:
        tt = i
print(abs(ss - tt))
