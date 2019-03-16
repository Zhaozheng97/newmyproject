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
    #创建空列表
    mlist = []
    #遍历列表去空格
    for i in klist :
        mlist += i.split()
    print(mlist)
    #放入set集合去重
    kset = set(mlist)
    #判断去重后的长度与去空格后的列表长度是否一样 否则有重复
    if len(kset) < len(mlist):
        print("有重复的字符串")

    #输出重复的字符
    print("重复的所有字符:{ksetkey}".format(ksetkey=kset))

    #将重复的键作为字典的键和值
    #创建空字典
    mdict = dict()
    #循环set集合将元素循环放入字典中
    for i in kset :
        mdict[i] = i
    print(mdict)

    #将重复的键作为键 出现的词频作为值
    #创建空字典
    mdict1 = dict()
    # 循环set集合将元素循环放入字典中
    for i in kset :
        mdict1[i] = mlist.count(i)
    print(mdict1)

