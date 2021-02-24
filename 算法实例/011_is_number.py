# 判断输入是否是有效数字

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


s = input("请输入一个字符串: ")
if is_number(s):
    print("{} 的值为 {}".format(s, float(s)))
else:
    print("{} 不是有效数字".format(s))
