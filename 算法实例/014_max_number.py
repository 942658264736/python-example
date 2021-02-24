# 获取输入中的最大值

str = input("请输入要比较的数字，使用空格分隔： ")
args = str.split(" ")
args = [int(arg) for arg in args]
print("{} 中的最大值是 {}".format(args, max(args)))
