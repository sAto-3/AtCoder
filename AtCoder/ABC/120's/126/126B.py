#B
s = input()
# print(int(s[0:2]), int(s[2:4]))
if 1 <= int(s[0:2]) <= 12 and 1 <= int(s[2:4]) <= 12:
    print('AMBIGUOUS')
elif 1 <= int(s[0:2]) <= 12:
    print('MMYY')
elif 1 <= int(s[2:4]) <= 12:
    print('YYMM')
else:
    print('NA')
