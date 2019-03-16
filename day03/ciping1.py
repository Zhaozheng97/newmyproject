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

    mlist = []
    for i in klist :
        mlist += i.split()
    print(mlist)
    kset = set(mlist)
    print(kset)
    mdict = dict()
    for i in kset:
        mdict[i] = mlist.count(i)
    print(mdict)

    if len(kset) < len(mlist):
        print("有重复")
    mdict1 = dict()

    for i in kset:
        mdict1[i]=i
    print(mdict1)