# D
n = int(input())
tree = [[] for _ in range(n)]

for i in range(n - 1):
    u, v, w = map(int, input().split())
    tree[u - 1] += [(v - 1, w % 2)]#treeが
    tree[v - 1] += [(u - 1, w % 2)]
# print(tree)

# 白:0 黒:1 未定:-1
color = [-1] * n
q = [(0, 0)]

while q:  # qが存在する間
    a, b = q.pop()
    color[a] = b  # a番目をb色に染める
    for c, d in tree[a]:
        if color[c] == -1:  # 行き先が捜索済みでない
            q += [(c, b ^ d)] #(行き先ｃ ,和が奇数の時１ 偶数 0)
print(*color, sep='\n')