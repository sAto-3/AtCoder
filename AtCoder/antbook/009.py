#区間スケジューリング問題
#仕事が重ならずに出来るだけ多くの仕事に参加したい。何個でられる？

#仕事をの終了時間が一番早い仕事を選ぶ
n = int(input())
st = [list(map(int, input().split())) for _ in range(2)]
st.sort(key=lambda x: x[1])
count = 1
left = st[1][0]
print(st,left)
for i in range(n):
    if st[0][i] > left:
        left = st[1][i]
        count += 1
    print(left)
print(count)