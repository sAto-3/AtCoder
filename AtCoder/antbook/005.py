# Lake Counting(深さ優先探索DFS)
# DFSを呼び出した回数を記録する
n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
def dfs(x, y):
    field[x][y] = "."

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if (0 <= nx < n and 0 <= ny < m and field[nx][ny] == "W"):
                dfs(nx, ny)
def solve():
    res = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == "W":
                dfs(i, j)
                res += 1
    print(res)
if __name__ == "__main__":
    solve()
