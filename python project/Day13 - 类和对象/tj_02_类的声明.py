



"""
类：就是拥有相同属性和相同功能的对象的集合
对象：类的实例

类的声明
class 类名(父类列表):
      类的内容

说明：
class - 声明类的关键字
类名 - 标识符，不能是关键字；采用驼峰式命名，并且首字母要大写


(父类列表) - 继承语法；可以省略，省略的时候相当于(object)
类的内容 - 主要包含属性和方法


"""





"""
属性和方法
类中的属性 - 指的是在类中声明的变量；分为类的字段和对象属性
类型的方法 - 指的是在类中声明的函数；分为对象方法，类方法和静态方法
"""

class Person:
    """人类"""
    num = 66
    def eat(self):
        print("吃")


"""
3.创建对象
类名() ---> 创建类对应的对象
"""
xiaoli = Person()
print(xiaoli)
print(xiaoli.eat())









