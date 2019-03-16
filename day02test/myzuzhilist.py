import random
if __name__ == '__main__':
    mynum = [3,7,4,2]

    #打乱顺序，导包 random
    random.shuffle(mynum)
    print(mynum)

    #对列表进行降序排列
    mynum.sort(reverse=True)
    print(mynum)