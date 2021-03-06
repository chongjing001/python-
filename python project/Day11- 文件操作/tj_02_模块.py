

"""
python 中一个文件就是一个模块

关联
方式一： impotr 模块名 - 将指定的模块导入当前模块中(模块名就是py文件的文件名)
说明：
a.执行import的时候，实质会进入指定的模块对应的py文件中，去执行里面的内容
b.import导入模块的时候，会检测当前模块之前是否已经导入过，如果已经导入就不在导入
c.通过import去导入一个模块后，可以通过 模块名.全局变量 去使用被导入模块中的内容



方式二：
from 模块名 import 变量名/函数名 - 导入模块中指定的变量和函数
说明：
a.执行到导入模块的语句的时候，还是会执行指定模块中的所有语句
b.通过from - import 导入的时候，导入多次还是只执行一次（查重）
c.使用的时候只能用import后面的变量/函数，而且用的时候不用在前面加模块名
d.import后面可以使用逗号将多个变量/函数隔开，也可以使用*号将模块中所有的全局变量一起导入
"""



# 重命名
"""
import 模块名 as 新模块名
form 模块名 import 变量名 as 新变量名


函数 - 对功能进行封装 - 获取当前时间对应的代码封装到函数中
模块 - 对多个功能和多个数据进行封装 - 将所有和xx相关的函数或变量放到一个py文件里
包 - 对多个模块进行封装  - 将所有和时间相关的朋友文件放到一个文件夹中
包：含有 __init__.py文件的文件夹

包的导入
import 包名    - 会直接执行摆钟的 __init__.py文件的内容
import 包名.模块名 - 导入包中指定的模块
from 包名 import 模块名
form 包名.模块名 import 变量

"""









