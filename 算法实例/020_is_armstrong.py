# 判断输入是否是阿姆斯特朗数
def is_armstrong(n):
    length = len(n)
    sum = 0
    for i in range(length):
        sum += 10 ** (length-i-1) * int(n[i])
    print("sum is {}".format(sum))
    if sum == int(n):
        return True
    else:
        return False


arg = input("请输入一个正整数：")
if is_armstrong(arg):
    print("{} 是阿姆斯特朗数".format(arg))
else:
    print("{} 不是阿姆斯特朗数".format(arg))
