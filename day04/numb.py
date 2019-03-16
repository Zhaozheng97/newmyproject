if __name__ == '__main__':
    i = 0
    sum = 0
    while i <= 100 :
        sum += i
        i += 1
    print(sum)

    num = 0
    for i in range(0,101) :
        num += i
    print(num)

    num1 = 0
    num1 = [num1+i for i in range(0,101)]
    print(num1)
