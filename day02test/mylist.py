if __name__ == '__main__':
    #内建结构--列表 [] 表示 逗号分隔 索引从0开始
    #两种创建方式
    mlist = list()
    mlist1 = []
    print(mlist1)
    print(mlist)

    #在列表尾部添加数据
    mlist.append("班长")
    print(mlist)

    #在列表指定位置添加数据
    mlist.insert(0,"学委")
    print(mlist)

    #删除整个列表
    #del mlist

    #从列表中删除指定数据，如果不存在 抛出异常 ValueError
    #mlist.remove("学")
    print(mlist)

    #如果不指定参数从列表中最后一个数据删除
    #mlist.pop()
    print(mlist)

    #mlist.pop(0)
    print(mlist)

    #清空数据但保留列表
    mlist.clear()
    print(mlist)