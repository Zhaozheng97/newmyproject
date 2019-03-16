if __name__ == '__main__':
    mstr = "good good study , day day up"

    #按" "空格进行分割 返回字符串列表
    mlist = mstr.split(" ")
    print(mlist)

    #按" "空格进行分割，分割次数一次 返回字符串列表
    mlist1 = mstr.split(" ",1)
    print(mlist1)