import random
if __name__ == '__main__':
    v1 = random.randint(0,1)
    print(v1)
    v2 = random.randrange(0,2)
    print(v2)
    v3 = ["aa","bb","cc"]
    random.shuffle(v3)
    print(v3)
    v4 = random.uniform(3,4)
    print(v4)