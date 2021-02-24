# 计算圆的面积
r = float(input("请输入圆的半径: "))
def circle_area(r):
  PI = 3.14
  return r ** 2 * PI

print("圆面积: {:.2f}".format(circle_area(r)))