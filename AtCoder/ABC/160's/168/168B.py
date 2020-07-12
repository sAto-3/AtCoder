#B
k = int(input())
s = input()
if len(s) <= k:
    print(s)
else:
    tmp = s[:k]
    print(tmp+"...")