if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    if len(klist)!=set(klist).__len__() :
        print("重复")
        #去空格
        mlist = []
        for i in klist:
            mlist+=i.split()
        mlist1 = [i for i in set(i for i in mlist)]
        for i in mlist1 :
            global mdict
            if mlist.count(i)>=2:
                mdict = {i:mlist.count(i)}
                print("重复的字符为{0},次数为{1}".format(i,mlist.count(i)))
    else:
        print("不重复")