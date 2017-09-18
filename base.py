#!/usr/bin/env python3 
# 在mac上面使用 可以直接执行./xxx.py
name = input('please enter your name: ')
print('hello', name)

print('1024 * 768 = ', 1024 * 768)

# 数据类型：
# 整数
a = 1
# 浮点数
a = 1.1
# 字符串
a = 'abc'
# 转义 \n 换行 \t 制表符
a = 'i\' am man'
# 布尔值 True False 注意首字母大写
# and or not 且或非 相当于JavaScript && || !
a = True
# 空值 None 相当于 JavaScript null NaN undefined 不等于0
a = None
# 变量
# 变量之间赋值是把变量b指向变量a所指向的数据 a改变了并不影响b
a = 'abc'
b = a 
a = 'XYZ'
print(b) # 'abc'
# 常量 通常用全部大写的变量名表示常量
PI = 3.1415926
# 除法运算 除法计算结果是浮点数
print(9 / 3) # 3.0
# 地板除 // 取整除法
print(10 / 3) # 3
# 余数运算 % 这点与JavaScript相同
print(10 % 3) # 1