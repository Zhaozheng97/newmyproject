if __name__ == '__main__':
    n = int(input("要生成的菱形："))
    for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
    for i in range(1,n):
        for j in range(1,i+1):
            print(end=" ")
        for j in range(1,n+1-i):
            print("*",end=" ")
        print()