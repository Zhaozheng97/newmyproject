if __name__ == '__main__':
    mone = int(input("输入第一个人的年龄："))
    mtwo = int(input("输入第二个人的年龄："))
    if mone > mtwo :
        print("第一个人的年龄较大，为：{monekey}".format(monekey=mone))
    elif mone == mtwo :
        print("两人年龄相同，为：{monekey}".format(monekey=mone))
    else:
        print("第二个人的年龄较大，为：{mtwokey}".format(mtwokey=mtwo))