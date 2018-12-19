
# 一旦一个字符串确定，那么字符串每一个字符的为值就确定了
# 而且每个字符会对应一个用来表示其位置和顺序的下标值

"""
1.下标（索引）
字符串中的每个字符都有一个下标，代表其在字符串的位置
下标的范围： 0 ~ 字符串长度-1
            -1 ~ -字符串长度（-1代表最后一个字符的下标）

2.获取单个字符
语法：字符串[下标] - 获取字符串中指定下标对应的字符
说明：字符串 - 可以是字符串常量，也可以是字符串变量（只要结果是字符串就行）
     下标 - 不能越界

3.获取部分字符
语法：字符串[开始下标:结束下标:步长]
功能：从开始下标开始获取到结束下标前为止，每次下标值增加对应的值
     返回的结果是字符串

注意：当步长是正数（从前往后取）、开始下标对应的字符要在结束下标对应字符的前面
    当步长是负数（从后往前取）、开始下标对应的字符要在结束下标对应字符的后面
"""
str1 = "1234567890"
print(str1[3:9:])
print(str1[3:9:2])

# 取不到
print("==：", str1[-1:6:2])

print("==:", str1[-6:6:-2])

# 简写：字符串[开始下标:结束下标] (相当于步长是1)
str2 = ""    # 空字符串

# 4.获取部分字符，省略下标
# 获取部分字符的时候，开始下标和结束下标都可以省略
"""
a. 开始下标省略   字符串[:结束下标:步长] 或者 字符串[:结束下标]
步长是正数：从字符串开头往后获取
步长是负数：从字符串结尾往前获取

b. 结束小标省略
   字符串[开始下标::步长]  后者 字符串[开始下标:]
   

"""

print(str1[:4:1])
print(str1[:4:-1])

print(str1[:])
print(str1[::-1])

print(str1[:100])