# if __name__ == '__main__':
#     str = "hello word"
#     mlist = [] #定义一个空的列表
#     mlist2 = [] #定义一个空的列表
#     mydict = {} #定义一个空的字典
#     for i in str : #遍历字符串把每个字符装到列表1中
#         mlist += i
#     mylist2 = set(mlist) #然后将列表1变成set集合除重 赋值给列表2
#     for l in mylist2 : #遍历列表2
#         if mlist.count(l) >= 2 : #判断列表1中与遍历列表2的字母相同的并且计数 大于等于2
#             mydict[l] = mlist.count(l) #将符合条件的赋值给字典
#     for k,v in mydict.items(): #遍历字典的Key 和 Value 显示出重复的字典
#         print("重复的字母为：{0} 出现次数为 {1} ".format(k,v)) #输出显示

# if __name__ == '__main__':
#     s = "sadkljfkljhasdjkfhas"
#     q = set()
#     for i in s:
#         q.add(i)
#     print(s.__len__() - q.__len__())
#     s="aabc"
#     d=set()
#     for i in s:
#         d.add(i)
#     for i in d:
#         num=s.count(i)
#         if num>=2:
#             print("重复的是{0},重复的次数为：{1}".format(i,num))