# 计算三角形面积
a = float(input("第一条边的长度:"))
b = float(input("第二条边的长度:"))
c = float(input("第三条边的长度:"))
s = (a + b+c)/2
area = (s * (s-a)*(s-b)*(s-c)) ** 0.5
print('三角形面积: %0.2f' %area)