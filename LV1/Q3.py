# 使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，
# 该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。
# 假设向程序提供以下输入:8
# 则输出为:
# {1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}


dict1 = {}


def generate_dict(n):
    for i in range(1, n+1):
        dict1[i] = i*i
    return dict1


print("请输入数字：")
x = int(input())
print(generate_dict(x))