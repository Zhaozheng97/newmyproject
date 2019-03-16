
def fun1():
    import day04.quest1.p1 as p1
    p1.checkSex()
    print()

def fun2():
    import day04.quest1.p2 as p2
    p2.unionSet()
    print()

def fun3():
    import day04.quest1.p3 as p3
    p3.emailVerify()
    print()

def fun4():
    import day04.quest1.p4 as p4
    p4.isReplyNumber()
    print()

if __name__ == '__main__':
    mdict1 = {#提示功能字典1
        1:"[1]输入用户姓名及性别，然后给出下列的提示",
        2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
        3:"[3]输入一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）",
        4:"[4]从键盘输入一行字符串，判断是否是回文数"
    }
    mdict2 = {#储存函数字典2
        1:fun1,
        2:fun2,
        3:fun3,
        4:fun4
    }

    while True:
        for i in mdict1.values() :#输出字典1提示内容
            print(i)

        msel = input("请选择功能")

        if msel == "q" :
            print("退出系统")
            break

        print()
        for k in mdict1.keys() :
            if int(msel) == k :
                print("你选择的是:{mdict1key}".format(mdict1key=k))
                print()
                mdict2[k]()#加()实现反向索引
