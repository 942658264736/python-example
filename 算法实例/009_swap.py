# 交换两个变量
x = input("输入 x 值: ")
y = input("输入 y 值: ")

print("交换前: x : {}, y: {}".format(x, y))
temp = x
x = y
y = temp
print("交换后: x : {}, y: {}".format(x, y))
