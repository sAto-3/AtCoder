#A
s=input()
t = input()
# print(t[:-1])
if len(s) + 1 == len(t) and t[:-1]==s:
    print('Yes')
else:
    print('No')