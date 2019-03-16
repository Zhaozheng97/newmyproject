if __name__ == '__main__':
    for i in range(1,10) :
        for j in range(1,10) :
            if j <= i :
                x = str(i*j)
                x = x.rjust(2," ")
                print(i,"*",j,"=",x,end=" ")
            else:
                print("")
                break