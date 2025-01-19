def is_blessed_id(A):
    # 预处理所有可能的平方数
    squares = set()
    i = 1
    while i * i <= 10 ** 9:
        squares.add(i * i)
        i += 1

    # 将数字A转换为数字列表
    digits = list(map(int, str(A)))

    # DFS函数，判断是否可以分割成平方数
    def dfs(idx):
        if idx == len(digits):
            return True

        num = 0
        for i in range(idx, len(digits)):
            num = num * 10 + digits[i]
            if num in squares:
                if dfs(i + 1):
                    return True
        return False

    # 调用DFS函数，判断是否可以分割成平方数
    return "Yes" if dfs(0) else "No"

A = int(input())
# 输出结果
print(is_blessed_id(A))