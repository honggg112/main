def dfs(n, s, x, y):
    if n == 1:
        return s[x][y]  # 如果只剩一个元素，直接返回该元素值
    if n == 0:
        return 0

    curr = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 右、下、左、上

    for i in range(4 * (n - 1)):
        dx, dy = directions[(i // (n - 1)) % 4]  # 根据当前索引计算方向
        x += dx
        y += dy
        curr += s[x][y]

    return max(curr, dfs(n - 2, s, x + 1, y + 1))  # 递归到下一层，矩阵缩小一圈，起始坐标向内移动一格

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
result = dfs(n, s, 0, 0)
print(result)