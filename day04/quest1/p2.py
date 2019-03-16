def unionSet() :
    import random
    mlist1 = [random.randint(1,21) for i in range(0, 10)]
    mlist2 = [random.randint(1,21) for i in range(0, 15)]

    mset = set(mlist1 + mlist2)

    print("第一个随机列表为：{mlist1key}".format(mlist1key=mlist1))
    print("第二个随机列表为：{mlist2key}".format(mlist2key=mlist2))
    print("两数列的并集为:{msetkey}".format(msetkey=mset))
