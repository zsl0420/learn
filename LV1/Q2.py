# 编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。
# 假设向程序提供以下输入:8
# 则输出为:40320

# 解法思路 1.递归函数 2.n 的阶乘 = n*(n-1)*....*1 3.0 的阶乘为1


def fact(n):
    if n == 0:
        return 1
    else:
        return (n*fact(n-1))


print("请输入一个数字：")
x = int(input())
print(fact(x))