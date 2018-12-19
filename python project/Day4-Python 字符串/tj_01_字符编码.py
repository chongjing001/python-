


# 字符串：序列，有序、不可变

# 1.字符编码
"""
python 中的字符采用的是Unicode编码

a.什么是编码：就是数字和字符的一一对应，其中字符对应的数字就是字符的编码

b.编码方式：
   ASCII码表：针对数字字符、字母字符、一些英文中常用的符号进行编码
            大写字母的ASCII值小于小写字母的值
            采用一个字节对字符进行编码（2**7 - 1）
   Unicode表：Unicode码包含ASCII码表，同时能够对世界上所用语言及对应符号进行编码
            采用两个字节对字符进行编码，能编码655536编码

            中文编码值：4E00 ~ 9FA5

c.两个函数
chr（编码值）- 将字符编码转化成字符
ord(字符) - 获取字符对应的编码值


"""

print(chr(0x004E00), chr(0x009FA5))
print(ord("童"))
# 可以将字符编码放到字符编码中就是一个字符： \u + 4位的16进制编码值
print(hex(31461))
print("cop\u7ae5>>>>>>")

