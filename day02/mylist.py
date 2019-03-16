if __name__ == '__main__':
    mlist = list()
    mlist2 = []
    print(type(mlist))
    print(type(mlist2))
    mlist.append("你好")
    print(mlist)
    mlist.insert(0,"我好")
    print(mlist)

    mlist2.append("你是?")
    print(mlist2)
    mlist2.insert(0,"woshi?")
    print(mlist2)
    print(mlist2.__len__())

    mlist.pop()
    print(mlist)

    del mlist2[0]
    print(mlist2)

    mlist2.remove("你是?")
    print(mlist2)

    mstr = "this wow"
    mstr=mstr.capitalize()
    print(mstr)