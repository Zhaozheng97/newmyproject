if __name__ == '__main__':
    mstr = "good good study , day day up"

    #该函数将指定字符串进行替换“good”替换为"gub"
    nstr = mstr.replace("good","gub")
    print(nstr)

    #第三个参数为max 可选可不选 如果指定 替换次数不能超过max次
    nstr1 = mstr.replace("good","gub",1)
    print(nstr1)