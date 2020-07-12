# C
n = int(input())
ans = []
while n > 26:
    # print(n)
    if n % 26 == 0:
        ans.append(26)
    else:
        ans.append(n % 26)
    if n <= 26:
        break
    n = (n - 1) // 26
ans.append(n)
ans.reverse()
# print(ans)
for i in ans:
    print(chr(i + 96), end='')
