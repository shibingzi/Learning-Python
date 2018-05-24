# -*- coding: utf-8 -*-
# 汉诺塔移动
def move(n, a, b, c):
    if n == 1:
        print(num(), a, '-->', c)
#        return count
    else:
        print(n)
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)
i = 0
def num():
    global i 
#在编写程序的时候，如果想为一个在函数外的变量重新赋值，
#并且这个变量会作用于许多函数中时，就需要告诉python这个
#变量的作用域是全局变量。此时用global语句就可以变成这个任务，
#也就是说没有用global语句的情况下，是不能修改全局变量的。
    i = i + 1
    return i
move(4, 'a', 'b', 'c')
print('共移动了(%d)次',num() - 1)
 