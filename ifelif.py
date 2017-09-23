#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

# x为非零、非空、非空list 非空元组 为true 和javascript判断不同多了一个非空list 一个非空元组
x = (1)
if x:
	print('true')

# 根据用户的输入 判断
s = input('birth: ')
# 获取到的是str 需要转化成int做比较
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')