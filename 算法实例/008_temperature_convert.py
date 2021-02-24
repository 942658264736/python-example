# 温度转换
arg = input("请输入温度: ")
temperature = float(arg[0:-1])
flag = arg[-1]

# 华氏度转换为摄氏度
def get_centigrade(f):
    return (f - 32) / 1.8


def get_fahrenheit(c):
    return c * 1.8 + 32


if flag in ['c', "C"]:
    print("摄氏度: {} F°".format(get_fahrenheit(temperature)))
elif flag in ['f', "F"]:
    print("华氏度: {} C°".format(get_centigrade(temperature)))
else:
    print("输入格式不正确!")
