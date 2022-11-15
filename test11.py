
# s = r"r'Hello\n Word'"
#
# print(s)
#
# k = r'''
#     <<<早发白帝城>>>
# 朝辞白帝彩云间,千里江陵一日还.
# 两岸猿声啼不住,轻舟已过万重山.
# '/n'  ''\n''
# '''
#
# print(k)


# print(int('100',36))
# aa = '111'
# print(36**2)
# i = 32
# s = 'i*i = {}'.format(i*i)
# print(s)
# t = '{0}    *    {0} = {1}'.format(i,i*i)
# print(t)

# class Dog:
#     #构造方法
#     def __init__(self,name1,age1):
#         self.name2 = name1
#         self.age2 = age1
#
#     #实例方法
#     def run(self):
#         print("{}在跑……".format(self.name2))
#     #实例方法
#     def speak(self,sound):
#         print("{}在叫,'{}'".format(self.name2,sound))
#
# d = Dog('球球',2)
# e = Dog('腿腿',1)
# print('我家的狗狗叫{0},{1}岁了!'.format(d.name2,d.age2))
# print('你家的狗狗叫{0},{1}岁了!'.format(e.name2,e.age2))
#
# d.run()
# d.speak("旺 旺 旺")

import datetime
tt = 0x793582aff
print(tt)
a = datetime.datetime.fromtimestamp(tt)
print(a)
print(datetime.datetime.fromtimestamp(999999999.999))
d = datetime.date.today()
print(d)

t = datetime.time(23,15,20,9999)
print(t)

delta = datetime.timedelta(weeks = -10)
# d +=delta
# print('d= {}'.format(d))
dd = datetime.datetime.today()
strd = dd.strftime('%Y-%m-%d %H--%M--%S---%f, %z---%Z')
print(strd)
