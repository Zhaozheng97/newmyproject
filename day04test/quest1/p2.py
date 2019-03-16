def soList():
    mlist = ["ab","a","abc","abcd","abcde","abcdef","abcdefg","abcdefgh","abcdefghi","abcde"]
    mlist.sort(key=lambda x:len(x))
    print(mlist)
