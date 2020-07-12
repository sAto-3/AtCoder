# 部分和問題
n = int(input())
a = list(map(int, input().split()))
k = int(input())

def dfs(i, sum):
    #n個集めたらkと比べる
    if i == n:
        return sum == k
    #a[i]を使わないとき
    if dfs(i + 1, sum):
        return True
    #a[i]を用いるとき
    if dfs(i + 1, sum + a[i]):
        return True
    return False

def solve():
    if dfs(0, 0):
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    solve()