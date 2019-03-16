if __name__ == '__main__':
    mstr = "u can u up, no zuo no die"

    #查看字符串是否以指定参数‘u’字符开头 如果是返回True 否则False
    mbool = mstr.startswith("u")
    print(mbool)

    #查看指定位置是否以'c'字符开头，下标2-4范围内查找
    mbool1 = mstr.startswith("c",2,4)
    print(mbool1)