# C
import itertools
n, m, x = map(int, input().split())
ca = [list(map(int, input().split()))for i in range(n)]
l = []
ans = 1e10
for i in range(1, n+1):
    for j in itertools.combinations(range(n), i):#ｎまでの組み合わせ
        # print(j)
        tmp = 0 #金額zc
        li = [0] * m#理解度li
        for k in j:#k番目の参考書
            # print(k)
            tmp += ca[k][0]#金額を加える
            for o in range(m):#場合jの時のkの参考書を読んだときの理解度を足す
                # print(o)
                li[o] += ca[k][o + 1]#理解度を足す
        # print(li)
        count = 0  #理解度カウンターm-1 まで
        for p in li:
            # print(count)
            if p >= x:#全ての理解度がx以上
                count += 1
            else:
                break
        # print(count,m)
        if count == m:#理解度カウンターがmになる
            # print(count,m,j)
            ans = min(ans, tmp)#金額が低い
if ans != 1e10:# 合計金額としては高すぎる>ならば一度も理解が追いついていない>-1
    print(ans)
else:
    print(-1)
