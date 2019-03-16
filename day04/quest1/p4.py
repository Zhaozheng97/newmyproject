def isReplyNumber():#也可以放到列表中进行反转
    msc = input("请输入一串数字，判断是否回文数：")
    if msc.__len__() % 2 == 1:
        sz = msc[::-1]
        if int(msc) == int(sz):
            print("是回文数")
        else:
            print("不是回文数")
    else:
        print("回文数必须是奇数位")
