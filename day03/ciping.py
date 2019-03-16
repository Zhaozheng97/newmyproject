if __name__ == '__main__':
    klist = [
    "good ","good ","study",
    " good ","good","study ",
    "good "," good"," study",
    " good ","good"," study ",
    "good ","good ","study",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
    " day ","day"," up",
         ]
    #把列表字符串去空格放入新列表
    mlist = [i.strip() for i in klist]
    #转成set集合去重
    kset = set(mlist)
    div1 = {}
    for i in kset:
        num=mlist.count(i)
        div1[i] = i
    print(div1)
    #判断是否重复
    if len(klist)>len(kset):
        print("字符有重复")
    #遍历放入字典
    div={}
    for i in kset:
        num=mlist.count(i)
        div[i] = num
    print(div)