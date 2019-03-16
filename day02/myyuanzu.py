if __name__ == '__main__':
    mytuple = (1,2,3,4,5)

    print("mytuple[{1}]={0}".format(mytuple[1],1))

    for i in mytuple :
        print(i)

    ntuple = mytuple[0:5:2]
    print("ntuple = ",ntuple)

    print(id(mytuple))
    print(id(ntuple))