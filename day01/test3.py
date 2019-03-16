if __name__ == '__main__':
    #九九乘法表
    ao = range(1,10)
    for i in ao :
        for j in ao :
           if j <= i :
               print(j,"*",i,"=",i*j , sep="",end =" ")
           else:
               print()
               break