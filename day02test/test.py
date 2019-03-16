if __name__ == '__main__':
    str = "are you ok?"
    mlist = [i for i in set(i for i in str)]
    for i in mlist :
        if str.count(i) >=2 :
            print("重复的字符为:{0} 次数为:{1}".format(i,str.count(i)))