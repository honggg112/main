d = int(input())
n = int(input())
board = [[0] * 1025 for _ in range(1025)]

for _ in range(n):
    x, y, k = map(int, input().split())
    for i in range(max(0, x - d), min(1025, x + d + 1)):
        for j in range(max(0, y - d), min(1025, y + d + 1)):
            board[i][j] += k

maxk = max(max(l) for l in board)
num = sum(l.count(maxk) for l in board)
print(num, maxk)