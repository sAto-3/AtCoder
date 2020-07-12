#B
n, m, q = map(int, input().split())
#解いた人の配列[m][n+1]
l = [[0 for _ in range(m)] for i in range(n + 1)]

for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        # スコアを表示 s[1]のスコア s[問題][x]
        # pass
        tmp = 0
        # s[1]列を観る
        for i in range(m):
            #1なら
            if l[s[1]][i] == 1:
                #得点にn-l[問題][0]
                tmp += n - l[0][i]
        print(tmp)
    if s[0] == 2:
        # スコア入力 s[1]がs[2]を解いた
        l[s[1]][s[2] - 1] = 1
        l[0][s[2] - 1] += 1
