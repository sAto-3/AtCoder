#B
a, b, k = map(int, input().split())
count = 0
ans = 0
c=[]
for i in range(1, 101):
    if a % i == 0 and b % i == 0:
        count += 1
        c.append(i)
print(c[-k])