# 判断输入数字的正负
num = float(input("请输入一个数字: "))
if num > 0:
    print("{} 是正数".format(num))
elif num < 0:
    print("{} 是负数".format(num))
else:
    print("{} 是零".format(num))
