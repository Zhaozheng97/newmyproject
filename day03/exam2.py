if __name__ == '__main__':
    mone = int(input("输入第一个人的出生月份"))
    mtwo = int(input("输入第二个人的出生月份"))
    if mone > 12 and mtwo >12 :
        print("请输入正确的出生月份")
    else:
        for i in range(0,13):
            if mone % mtwo == i :
                if i == 1 :
                    print("非常有缘")
                elif i == 2 :
                    print("比较有缘")
                elif i == 3 :
                    print("缘分一般")
                elif i == 4 :
                    print("有仇")
                else:
                    print("无缘亦无仇")