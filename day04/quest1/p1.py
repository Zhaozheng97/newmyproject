def checkSex():
    mname = input("输入用户姓名")
    msex = input("输入用户性别")
    mdict = dict()
    if msex == "男" or msex == "man" or msex == "nan" :
        mdict = {msex:"先生"}
        print("{mnamekey}{mdictkey}你好".format(mnamekey=mname, mdictkey=mdict[msex]))
    elif msex == "女" or msex == "woman" or msex == "nv" :
        mdict = {msex:"女士"}
        print("{mnamekey}{mdictkey}你好".format(mnamekey=mname, mdictkey=mdict[msex]))
    else:
        print("输入有误")
