import math

while True:
    N = int(input())
    if N == 0:
        break

    max_time = float("inf")
    for i in range(N):
        Vi, Ti = map(int, input().split())
        if Ti < 0:
            continue
        arrival_time = math.ceil((4.5/ Vi) * 3600 + Ti)
        max_time = min(max_time, arrival_time)

    print(max_time)