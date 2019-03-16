#技能1
# if __name__ == '__main__':
#     name = input("输入你的姓名:")
#     sex = input("输入你的性别:")
#     age = input("输入你的年龄:")
#     print("我是{name},性别{sex},今年{age}了".format(name = name , sex = sex , age = age))

#技能2
# import math
# if __name__ == '__main__':
#     ca = input("输入一个数字:")
#     a = int(ca)
#     math.sqrt(a)
#     print(a)

#技能3
import random
if __name__ == '__main__':
    sc = input("输入一个整数")
    sa = random.randint(0,10)
    sc = int(sc)
    if sc == sa :
        print("两数相同")
    if sc > sa :
        print("输入的数大，为:{0}".format(sc))
    if sc < sa :
        print("随机数比较大，为:{0}".format(sa))