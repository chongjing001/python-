

"""
1.对象方法
直接声明在类中，并且自带一个叫self的参数的函数

2.对象方法的调用 - 通过对象调用对象的方法
对象.对象方法

3.self（当前对象）
通过对象调用的对象的方法，对象方法中的第一个参数self不用传参
系统会自动将当前对象传给self
那个对象调用的，self就指向谁
"""


class Person:
    """人类"""
    def sleep(self):
        print("睡")

p1 = Person()



