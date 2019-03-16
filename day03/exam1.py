if __name__ == '__main__':
    mdate = input("请输入一个日期，格式为（20190314）：")
    y = int(mdate[0:4])#获取年
    m = int(mdate[4:6])#获取月
    d = int(mdate[6:])#获取日

    flag = False
    if y % 100 == 0 :
        if y % 400 == 0 :
            flag = True
        else:
            flag = False
    elif y % 4 ==0 :
        flag = True
    else:
        flag = False
    md = 0
    my = []
    if flag == True :
        my = [31,29,31,30,31,30,31,31,30,31,30,31]
        for i in range(1,13) :
            if int(m) == i :
                for j in range(i-1) :
                    md += my[j]
        print("这一天是{ykey}年中的第{mdkey}天".format(ykey=y,mdkey=md+d))
    else:#平年
        my = [31,28,31,30,31,30,31,31,30,31,30,31]
        for i in range(1,13) :
            if int(m) == i :
                for j in range(i-1) :
                    md += my[j]
        print("这一天是{ykey}年中的第{mdkey}天".format(ykey=y,mdkey=md+d))
