def moveHanoi(n, from_rod, to_rod, mid_rod):
    if n == 0:
        return
    # 将前n-1个盘子从from_rod移动到mid_rod，借助to_rod作为辅助
    moveHanoi(n - 1, from_rod, mid_rod, to_rod)
    # 将第n个盘子从from_rod直接移动到to_rod
    print(f"{from_rod}->{to_rod}")
    # 将前n-1个盘子从mid_rod移动到to_rod，借助from_rod作为辅助
    moveHanoi(n - 1, mid_rod, to_rod, from_rod)

n = int(input())
# 计算最少移动次数
print(2**n - 1)
# 调用递归函数，开始移动盘子
moveHanoi(n, 'A', 'C', 'B')