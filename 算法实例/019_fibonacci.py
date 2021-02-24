# 获取斐波那契值 0 1 1 2 3 5
def fibnacci(n):
  # 该函数可以通过递归实现,但计算到
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # 这里不能使用递归,可以试试计算下fibnacci(40)的结果,为什么不能使用递归
        # return fibnacci(n-1) + fibnacci(n-2)
        pre = 0
        cur = 1
        while n >= 2:
            n -= 1
            temp = pre + cur
            pre = cur
            cur = temp
        return cur


n = int(input("获取第几个斐波那契数: "))
n -= 1
print(fibnacci(n))
