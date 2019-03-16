if __name__ == '__main__':
    mstr = "10"

    #将字符串按照指定长度10进行左对齐，剩余部分用“-”补全 如果不指定填充字符默认为空格
    nstr = mstr.ljust(10,"-")
    print(nstr)