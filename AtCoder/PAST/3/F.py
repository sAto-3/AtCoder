#???
from collections import Counter
n = int(input())
s = [list(input()) for _ in range(n)]
print(s)
ans=False
#縦
for i in range(n):
    #縦
    a = True
    aa = []
    aaa=0
    #横
    b = True
    bbb=0
    for j in range(n):
        #縦
        aa.append(s[j][i])
    print([j for j in aa if aa.count(j) % 2 == 0])
    print([j for j in aa if aa.count(j) % 2 != 0])
    print([j for j in s[i] if s[i].count(j) % 2 == 0])
    print([j for j in s[i] if s[i].count(j) % 2 != 0])
    if (len([j for j in aa if aa.count(j) % 2 == 0]) > 0 and n % 2 == 0)\
    or(len([j for j in aa if aa.count(j) % 2 != 0]) == 1 and n % 2 == 1):
        ans = True
        print(*aa, sep='', end='')
    if (len([[j for j in s[i] if s[i].count(j) % 2 == 0]]) > 0 and n % 2 == 0)\
    or (len([[j for j in s[i] if s[i].count(j) % 2 != 0]]) == 1 and n % 2 == 1 and len([[j for j in s[i] if s[i].count(j) % 2 == 0]]) > 0):
        ans = True
        print(*s[i], sep='', end='')
if ans == False:
    print(-1)
