# 进制转换
# 1.十进制
"""
基数：0~9
进位：逢十进一
位权：123 = 100 + 20 + 3 = 1*10^2 + 2*10^1 + 3*10^0
"""

# 2.二进制(0b或0B)
print(0b10010)
"""
基数：0、1
进位：逢二进一
位权：1101 = 1*2^0 + 0*2^1 + 1*2^2 + 1*2^3

"""

# 3.八进制(0o或0O)
print(0o10010)
"""
基数：0~7
进位：逢八进一
位权：20 = 2*8^1 + 0*8^0
"""

# 4.十六进制(0x或0X)
print(0x10010)
"""
基数：0~9 + a~f
进位：逢十六进一
位权：123 = 3*16^0 + 2*16^1 + 1*16^2
"""

# 5.十进制数转其他进制
num = int(input("输入的十进制数"))
print(num)
print("转换为二进制", bin(num))
print("转换为八进制", oct(num))
print("转换为十六进制", hex(num))
"""
二进制转换为八进制，可以从后向前每三位转一位（位数不足用0补）
1 001 010 001（2）=1211 （8）

八进制转二进制，每一位八进制，转换成3位的二进制
56 = 110 111
二进制转十六进制，每4位转一位
10 0101 0001 (2) = 152

十六进制转二进制，每一位的十六进制，转换成4位的二进制
64 = 1100100 
"""
# 函数bin,oct,hex 返回的结果都是字符串类型

print(0b100)
