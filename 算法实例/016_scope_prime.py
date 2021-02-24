# 获取输入范围内的所有质数

def is_preme(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


min = int(input("请输入范围下限: "))
max = int(input("请输入范围上限: "))
primes = []
for i in range(min, max):
    if is_preme(i):
        primes.append(i)

print("素数: {}".format(primes))
