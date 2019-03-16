if __name__ == '__main__':
    #源数据 字符串下标从0开始
    mstr = "good good study , day day up"
    #在字符串中寻找“good”子字符串
    mindex = mstr.find("good")
    #该函数返回找到的字符串的起始下标
    print(mindex)

    #指定了从源字符串起始下标1开始查找“good”
    mindex1 = mstr.find("good",1)
    print(mindex1)

    #从源字符串起始下标1开始查找 到源字符串4结束 如果没有找到返回-1
    mindex2 = mstr.find("good",1,5)
    print(mindex2)