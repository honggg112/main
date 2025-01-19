"""
number = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
code_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
def verify_id_card(id_card):
    total_sum = sum(int(id_card[i]) * number[i] for i in range(17))
    return "YES" if code_map[total_sum % 11] == id_card[-1].upper() else "NO"

n= int(input())
for _ in range(n):
    print(verify_id_card(input().strip()))
"""
# 老师答案更好理解

# 定义权重数组
l = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
n = int(input())
code_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

for _ in range(n):
    s = input()
    if len(s) != 18:  # 检查输入字符串的长度
        print('NO')
        continue

    # 计算校验码
    x = sum(int(s[i]) * l[i] for i in range(17)) % 11

    # 比较校验码
    if s[17] == code_map[x]:
        print('YES')
    else:
        print('NO')