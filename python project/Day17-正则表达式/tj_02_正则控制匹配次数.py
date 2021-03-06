import re

"""
# 1 *(匹配0次或者多次)
用法： a* - a出现0次或者多次   "","a","aaa"...
\d* - 任意数字出现0次或者多次，"","1","12"...
[abc]* - a,b,c出现0次或者多次
[a-z]* - 小写字母字符出现0次或者多次
注意：在[]外面的*的前面需要一个字符或者一个匹配字符的符号
"""
print(re.fullmatch(r"a*b", "b"))

"""
2 +(匹配1次或者多次)
a+ - a至少出现一次
"""

"""
3 ? (匹配0次或者1次)
a? - a出现0次或者1次   "","a"可以匹配
"""
# 写一个正则表达式匹配一个整数（正负都可以）
re_str = r"[+-]?[1-9]\d*"
result = re.fullmatch(re_str, "-100")
print(result)

# {}
"""
{N} - 匹配N次，a{3} : 匹配3个"a"
{M,N} - 匹配M到N次，  例如 a{3,5} 匹配三个"a" 或者4个"a"或者5个"a"
{,N} - 最多匹配N次（0~N次）
{M,} - 至少匹配M次  例如：a{3,}
"""
# 输入密码，要求检测密码输入是否合格（字母和数字组成，数字不开头，6-12位）
pwd = "[a-zA-Z][\da-zA-Z]{5,11}"
result = re.fullmatch(pwd, "ds15s4d56")
if result:
    print("输入成功")
else:
    print("输入有误！！！")
