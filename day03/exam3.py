import random
if __name__ == '__main__':
    mnum = ""
    mnum1 = ""
    for i in range(0,9):
        mnum += str(random.randint(0,10))
    print("随机序列为",mnum)
    mnum1 = str(random.randint(0,10))
    print("随机整数位",mnum1)
    mm = mnum.find(mnum1)
    if mm == -1 :
        print("不存在")
    else:
        print("存在")