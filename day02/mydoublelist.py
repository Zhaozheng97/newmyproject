if __name__ == '__main__':
    mlist = [[7,8,9],[4,5,6],[1,2,3]]
    for i in mlist :
        for j in i :
            print("mlist[{1}]={0}".format(j,j.__index__()))