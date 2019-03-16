if __name__ == '__main__':
    mstr = "good good study , day day up"
    #该方法返回子字符串在字符串中出现的次数。
    mcount = mstr.count("good")
    print(mcount)

    #从下标1开始查找
    mcount1 = mstr.count("good",1)
    print(mcount1)

    #从下标1开始查找 到下标4结束 找不到返回0
    mcount2 = mstr.count("good",1,4)
    print(mcount2)