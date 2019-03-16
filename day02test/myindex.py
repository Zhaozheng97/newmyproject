if __name__ == '__main__':
    mstr = "good good study , day day up"
    mindex = mstr.index("good")
    print(mindex)

    mindex1 = mstr.index("good",1)
    print(mindex1)

    #index函数和find函数一样，但是如果找不到字符串则抛出异常 ValueError
    mindex2 = mstr.index("good",1,5)
    print(mindex2)