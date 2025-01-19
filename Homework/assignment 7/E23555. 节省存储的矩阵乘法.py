n, m1, m2 = map(int, input().split())
a = [[0] * n for _ in range(n)]
b = [[0] * n for _ in range(n)]
for _ in range(m1):
    x, y, v = map(int, input().split())
    a[x][y] = v
for _ in range(m2):
    x, y, v = map(int, input().split())
    b[x][y] = v
c = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        c[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
        if c[i][j] != 0:
            print(i, j, c[i][j])

"""
from collections import defaultdict

# 输入处理并将稀疏矩阵表示成字典
def read_matrix(num_nonzero):
    matrix = defaultdict(dict)
    for _ in range(num_nonzero):
        row, col, value = map(int, input().split())
        matrix[row][col] = value
    return matrix

# 稀疏矩阵乘法计算
def sparse_matrix_multiplication(n, X, Y):
    result = defaultdict(int)

    # 遍历矩阵X的每个非零元素
    for i in X:
        for k in X[i]:
            if k in Y:
                for j in Y[k]:
                    result[(i, j)] += X[i][k] * Y[k][j]

    # 过滤掉零值
    result = {key: value for key, value in result.items() if value != 0}
    return result

# 主程序
if __name__ == "__main__":
    n, m1, m2 = map(int, input().split())
    X = read_matrix(m1)
    Y = read_matrix(m2)

    # 计算乘积
    result = sparse_matrix_multiplication(n, X, Y)

    # 输出结果，按行号和列号排序
    result = sorted(result.items())
    print(len(result))
    for (row, col), value in result:
        print(row, col, value)
"""