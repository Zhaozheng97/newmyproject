if __name__ == '__main__':
    mstr = "u can u up , no can no 13 B"

    #查看字符串中是否以指定字符结尾 返回值是布尔值
    mbool = mstr.endswith("B")
    print(mbool)

    #指定查找范围，从 下标3 开始 到字符串末尾
    mbool1 = mstr.endswith("B",3,mstr.__len__())
    print(mbool1)