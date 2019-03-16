if __name__ == '__main__':
    i = range(0,101)
    for i in i :
        print(str(i).rjust(3, " "),end="")
        if i % 10 == 9 :
            print()
#使0-100整齐排列 每行10位数