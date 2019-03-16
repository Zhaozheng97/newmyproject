if __name__ == '__main__':
    mstr = "0.1"

    #将字符串按照长度10进行右对齐，“-”补全 如果不写补全参数 则默认空格代替
    nstr = mstr.rjust(10,"0")
    print(nstr)