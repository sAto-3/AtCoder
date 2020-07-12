from collections import deque
import math
n, m = map(int, input().split())
maping = [input() for _ in range(n)]
sx = 0
sy = 0
gx = 0
gy = 0
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
d = [0] * (n, m)

def BFS():
    q=deque()
    for i in range(n):
        for j in range(m):
            d[i][j] = math.inf()
    q.append((sx, sy))
    d[sx][sy] = 0
    while q:
        px, py = q.pop()
        if px == gx and py == gy:
            break
        
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            
            if 0 <= nx <= n and 0 <= ny <= n and mapint[nx][ny] != "#" and d[xy][ny] == INF:
                q.append((nx, ny))
                d[nx][ny] = d[px][py] + 1
    return d[gx][gy]

def solve():
    res = bfs()
    print(res)
    