if __name__ == '__main__':
    mlist = [i*i for i in range(0,11) if i % 2 == 1]
    print(mlist)

    mlist1 = [n + m for m in ["a","b","c"] for n in ["1","2","3"]]
    print(mlist1)

    L = ['Hello', 'World', 12.5, 'IBM', 'Apple', 6]
    l = [i.lower() for i in L if isinstance(i,str)]
    print(l)

    for i in L :
        if isinstance(i,str) :
            print(i.lower())