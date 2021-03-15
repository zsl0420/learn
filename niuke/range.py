# range的用法
# 题目 求下面的输入：
for i in range(2):
    print(i)

for i in range(4, 6):
    print(i)

# 解析： 这题主要考察range() 的用法
"""
range()函数语法为： range(start, end[, step])
start ：计数从start开始。默认是从0开始，可以不写，例如range(5)等价于range(0, 5);
end：计数到end 结束，但不包括end！！！，例如range(0, 5)输入[0, 1, 2, 3, 4]
step：步长，默认值为1，就是中间隔几个数输入下一个
"""
