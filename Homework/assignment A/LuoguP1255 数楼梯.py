n = int(input())
#定义，输入
a=1
#初始的变量赋值
b=1
n-=1

if n > 0 :
#判断，第6,7很坑的
    while n>0 :
        c=a+b
        a=b
        b=c
        n-=1
    print(b)
elif n == 0 :
#判断边界
        print(a)
else :
    a-=1
    #判断边界
    print(a)