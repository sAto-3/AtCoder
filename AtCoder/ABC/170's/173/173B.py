#B
n = int(input())
s = [input() for _ in range(n)]
ac = 0
wa = 0
tle = 0
re = 0

for i in s:
    if i == "AC":
        ac += 1
    if i == "WA":
        wa += 1
    if i == "TLE":
        tle += 1
    if i == "RE":
        re += 1

print('AC x' , ac)
print('WA x' , wa)
print('TLE x' , tle)
print('RE x' , re)