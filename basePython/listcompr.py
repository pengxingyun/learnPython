#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式

# 生成 1-10 平方的集合

print([x * x for x in range(1, 11)]) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 在上面的基础上加个只要偶数的条件
print([x * x for x in range(1, 11) if x % 2 == 0]) # [4, 16, 36, 64, 100]

# 双重循环 形成全排列
print([m + n for m in 'ABC' for n in 'XYZ']) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列表生成式 可使用多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()]) # ['x=A', 'y=B', 'z=C']

# 把list的所有字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L]) # ['hello', 'world', 'ibm', 'apple']

L1 = ['Hello', 'World', 18, 'Apple', None]

# 先判断列表项 如果是str 再转换为小写
print([s.lower() for s in L1 if isinstance(s, str)])