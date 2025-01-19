n= int(input())
friends= list(map(int,input().split()))
a= friends.count(1)
b= friends.count(2)
c= friends.count(3)
d= friends.count(4)

#4人小组直接各坐一辆
taxi = d

#各3+1 坐一辆
taxi += min(a,c)
remaining_3 = c- min(a,c)
remaining_1 = a- min(a,c)
#剩下的三个组各坐一辆
taxi += remaining_3

#两组2人组坐一辆
taxi += b//2
#多余的一个2人组+ 2个剩下的一人组
if b%2:
    taxi += 1
    remaining_1 = remaining_1 -2

#剩余的一人组坐一辆
taxi += (remaining_1 +3)//4

print(taxi)