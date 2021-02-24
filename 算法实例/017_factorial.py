# 计算阶乘
def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n-1) * n


n = int(input("请输入一个数字: "))
print("{}! = {}".format(n, factorial(n)))
