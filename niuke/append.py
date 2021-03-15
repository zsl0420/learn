nl = [1, 2, 5, 3, 5]

nl.append(3)
nl.insert(0, 7)
nl.sort()


print(nl)

# 答案为 ：[1, 2, 3, 3, 5, 5, 7]
"""
解析：这里主要考察append(), insert(), sort()的用法
append():在列表末尾增加一个数据项
extend():在列表末尾增加一个数据集合
insert(n, m):在索引为n的位置增加一个数据项m
sort():表示对自身排序
"""
