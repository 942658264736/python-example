# 最大公约数

list = eval(input("请输入一个数组： "))
divisor = 1
for i in range(2, min(list)):
    if all(elem % i == 0 for elem in list):
        divisor = i
print("{} 中最大的公约数是 {}".format(list, divisor))
