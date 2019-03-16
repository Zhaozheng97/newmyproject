import random
if __name__ == '__main__':
    mlist = []
    for i in range(0,10) :
        mlist +=str(random.randint(0,10))
    print("原序列为：",mlist)
    print("升序排列后为",sorted(mlist))