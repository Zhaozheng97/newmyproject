import random
if __name__ == '__main__':
    mlist = ""
    for i in range(0,10) :
        mlist += str(random.randint(0,10))
    print("随机序列为：{mlistkey}".format(mlistkey=mlist))
    mm = ""
    for i in range(0,10):
        mm = str(random.randint(0,10))
    print(mm)

    if mlist.find(mm) != -1 :
        print("存在")
    else:
        print("不存在")