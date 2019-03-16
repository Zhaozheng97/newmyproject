if __name__ == '__main__':
    n = int(input("请输入行数："))
    for i in range(1, n):#循环4次 n=5 i = 1 2 3 4
        for j in range(1, n - i):# n = 5 i = 1 2 3 4  j = 3 2 1 0
            print(end=" ") #3 2 1 0 个空格 不换行
        for a in range(1, i + 1): # i = 1 2 3 4  a= 1 2 3 4
            print("*", end=" ")# 1 2 3 4 个 * 不换行
        print()#换行4次

    #相比上边的等腰三角形 少一行
    for b in range(2, n):
        for c in range(2, b + 1):
            print(end=" ")
        for d in range(b, n):
            print("*", end=" ")
        print()