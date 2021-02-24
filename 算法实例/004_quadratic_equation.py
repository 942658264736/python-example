# 解一元二次方程
a = float(input("输入 a: "))
b = float(input("输入 b: "))
c = float(input("输入 c: "))
print("方程： {} x² + {} x + c = 0".format(a, b, c))
d = b**2 - 4 * a * c
result1 = (-b + d**0.5) / (2*a)
result2 = (-b - d**0.5) / (2*a)
print("解1：{}".format(result1))
print("解2：{}".format(result2))
