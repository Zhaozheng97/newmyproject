# if __name__ == '__main__':
#     try:
#         print(5/1)
#     except ZeroDivisionError as e :
#         print(e)
#     except Exception as e :
#         print("my Exception")
#         print(e)
#     else:
#         print("计算结束")

class MyExcept (Exception) :

    def end(self):
        print(" 11 ")

if __name__ == '__main__':
    try:
        print(5/0) #触发异常打印2
        print(5/f) #触发异常打印3
        raise MyExcept #自定义异常的出发条件 触发异常打印 1

    except MyExcept as e:#自定义异常
        print(e)
        e.end()
    except ZeroDivisionError as e :#除数为0异常
        print(e)
        print("2")
    except Exception as e :#自定义异常继承的父类异常（最大异常）
        print(e)
        print("3")
    else:
        print("程序无错")
    finally:
        print("程序完毕")
