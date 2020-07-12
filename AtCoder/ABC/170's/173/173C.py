#C
# x^12= 4096
h, w, k = map(int, input().split())
c = [input() for _ in range(h)]
ans = 0
for i in range(2 ** h):
    
    T = [c[j] for j in range(h) if (i >> j) & 1]
    #iをjだけシフトしたときが1である時のcの配列の集まり -> 塗る列
    for j in range(2 ** w): #塗る行数
        x = 0
        #行で見る
        for m in range(w):
            #選んだマスの行を塗る
            #mビットシフトした値と1のANDが1である -> mビット目が1である
            if (j >> m) & 1:
                for n in range(len(T)):
                    if T[n][m] == "#":
                        x += 1
        # 選択したマスの#の数がk個
        if x == k:
            ans += 1
print(ans)