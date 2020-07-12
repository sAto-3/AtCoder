#素因数分解(2以降)
def factorization(n):
    arr = []
    tmp = n
    #2から√n でnを割る ･･･割れた回数を指数として追加
    # for i in range(2, int(n ** 0.5 // 1) + 1):誤差が発生しそう
    i=1
    while i * i <= n:#修正後
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
        i += 1
    if tmp != 1:  #割り切れなかったとき
        arr.append([tmp, 1])
    if arr == []: #素数の場合(割れなかった場合)
        arr.append([n, 1])
    return arr

#公約数列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
#最大公約数
def gcd(a, b):
    while b != 0:
        if a < b:
            b, a = a, b
        a, b = b, a % b
    return a
#最大公倍数
def lcm(a, b):
    return a * b // gcd(a, b)