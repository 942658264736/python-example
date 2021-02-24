# 判断是否是闰年
def is_leaf(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True


year = int(input("请输入判断年份: "))
if is_leaf(year):
    print("{} 年是闰年".format(year))
else:
    print("{} 年是平年".format(year))
