#A
n = int(input())
n = n % 1000
if n == 0:
    n = 1000
print(1000-n)