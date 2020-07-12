s = list(input())
a = 0
b = 0
c = 0
for i in range(len(s)):
    if s[i] == "a":
        a += 1
    if s[i] == "b":
        b += 1
    if s[i] == "c":
        c += 1
# print(a,b,c)
if a > b and a > c:
    print("a")
elif b > a and b > c:
    print("b")
elif c > a and c > b:
    print("c")