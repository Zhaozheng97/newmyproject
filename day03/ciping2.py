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
    #去空格
    mlist = []
    for i in klist :
        mlist += i.split()
    print(mlist)
    #放入set
    kset = set(mlist)
    #判断是否有重复
    if len(klist) > len(kset) :
        print("有重复的字符串")
    print("重复的字符串为：{ksetkey}".format(ksetkey = kset))

    #把下面的klist作为字典的键
    #同时作为字典的值
    mdict = dict()
    for i in kset :
        mdict[i] = i
    print(mdict)

    # 把下面的klist作为字典的键
    # 并统计每个单词的词频
    mdict1 = dict()
    for i in kset :
        mdict1[i] = mlist.count(i)
    print(mdict1)