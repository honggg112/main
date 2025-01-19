def dfs(x, y, now_value):
    global max_value, opt_path
    # 如果到达右下角，更新最大权值和最优路径
    if x == n - 1 and y == m - 1:
        if now_value > max_value:
            max_value = now_value
            opt_path = temp_path[:]
        return

    # 标记当前位置为已访问
    visited[x][y] = True

    # 尝试向四个方向移动
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            next_value = now_value + maze[next_x][next_y]
            temp_path.append((next_x, next_y))
            dfs(next_x, next_y, next_value)
            temp_path.pop()  # 回溯

    # 取消当前位置的访问标记
    visited[x][y] = False

# 读取输入
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 初始化变量
max_value = float('-inf')
opt_path = []
temp_path = [(0, 0)]
visited = [[False] * m for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 从左上角开始DFS搜索
dfs(0, 0, maze[0][0])

# 输出最优路径
for x, y in opt_path:
    print(x + 1, y + 1)