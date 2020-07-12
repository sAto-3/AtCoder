#D
import heapq#heapqで優先度付きキューを使うことができる ...ヒープソートを用いた
n, m = map(int, input().split())
a= list(map(lambda x: int(x) * (- 1), input().split()))
heapq.heapify(a)  #優先度つきキューに移動

for i in range(m):
    tmp=heapq.heappop(a) * -1  #最大値の取り出し
    tmp //= 2
    heapq.heappush(a, -1 * tmp) #値の挿入(全体が-1倍になっているので注意)
print(sum(a)*-1)

