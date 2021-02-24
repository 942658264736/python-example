# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        # \t表示下一个tab的位置,通常是四个空格
        # end='' 表示不换行,默认end是"\n"
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()
