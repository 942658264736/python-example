# 判断是否是质数

def is_preme(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number = int(input("请输入一个正整数: "))
if number <= 0:
    print("输入不正确!")
else:
    if is_preme(number):
        print("{} 是质数".format(number))
    else:
        print("{} 不是质数".format(number))
