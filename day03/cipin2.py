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
    mlist = [i.strip() for i in klist]
    mdict = {i:mlist.count(i) for i in mlist}
    print(mdict)

    mlist1 = [i.strip() for i in klist]
    print(mlist1)
    mdict1 = {i:mlist.count(i) for i in mlist1}
    print(mdict1)