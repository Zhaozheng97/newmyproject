def nineTable():#九九乘法表
    for x in range(1,10) :
        for y in range(1,10):
            if y <= x :
                z = str(x*y)
                z = z.rjust(2," ")
                print(x,"*",y,"=",z,end=" ")
            else:
                print()
                break

def equalTriangle():#等边三角形
    for x in range(1,6):
        for y in range(1,6):
            print("*",end=" ")
            if x == y :
                print()
                break

def numberArray():#随机输入数字进行规则排列
    en = int(input("请输入要排列到的位置，从0开始:"))
    for i in range(0,en) :
        print(str(i).rjust(4," "),end=" ")
        if i % 10 == 9:
            print()

if __name__ == '__main__':
    nineTable()
    equalTriangle()
    numberArray()